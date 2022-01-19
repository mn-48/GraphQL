from dataclasses import field
import graphene

from graphene_django import DjangoObjectType
from quiz.models import Category, Quizzes, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizessType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")
    
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "date_created", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id","question", "answer_text", "is_right")


class Query(graphene.ObjectType):
    
    all_category = graphene.List(CategoryType)
    all_quiz = graphene.List(QuizessType)
    all_questions = graphene.List(QuestionType)
    all_answer = graphene.List(AnswerType)

    def resolve_all_category(self, info):
        return Category.objects.all()
    
    def resolve_all_quiz(self, info):
        return Quizzes.objects.all()

    def resolve_all_questions(self, info):
        return Question.objects.all()

    def resolve_all_answer(self, info):
        return Answer.objects.all()

    
schema = graphene.Schema(query=Query)