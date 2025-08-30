from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Question, Answer


class QuestionTestClass(TestCase):
    def setUp(self):
        question = Question.objects.create(text="Hello World!")
        user = User.objects.create_user(username='test', password='test')
        Answer.objects.create(text="Hello World!", user=user, question=question)

    def test_add_question(self):
        response = self.client.post(
            reverse("question_list"),
            {
                    "text": "test",
                  })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Question.objects.filter(text="test").exists())

    def test_list_questions(self):
        response = self.client.get(reverse("question_list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["text"], "Hello World!")

    def test_question_id(self):
        response = self.client.get(reverse("question-detail", kwargs={"pk": 1}))
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["text"], "Hello World!")

    def test_delete_question(self):
        response = self.client.delete(reverse("question-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Answer.objects.filter(pk=1).exists())





class AnswerTestClass(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='test')
        Question.objects.create(text="Hello World!")

    def test_add_answer(self):
        response = self.client.post(reverse("answer-create", kwargs={"pk":1}),
                                    {"text": "Hello World!",
                                     "user": 1,
                                     "question": 1})
        self.assertEqual(response.status_code, 201)
        answer = Answer.objects.get(pk=1)
        self.assertEqual(answer.question.id, 1)

    def test_answer_id(self):
        self.client.post(reverse("answer-create", kwargs={"pk":1}),
                                    {"text": "Hello World!",
                                     "user": 1,
                                     "question": 1})
        response = self.client.get(reverse("answer-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)



