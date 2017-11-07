# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Userprofile,QandA,options,answer,User,Profile,Comments,Replies
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .forms import UserForm,Qtn
from django.db import connection,transaction
from datetime import datetime as dt

cursor = connection.cursor()
# Create your views here.
def index(request):
      if request.method == 'POST':
            row = QandA.objects.raw('Select * from QandA ')
            userdetail  = row
            context = {'userdetail' : userdetail}

            return render(request,'uProfile/index.html',context)



def details(request,Userprofile_id):
      userdetail = get_object_or_404(Userprofile,pk = Userprofile_id)
      return render(request,'uProfile/detail.html',{'userdetail' : userdetail})

class QuestionAdd(CreateView):
      model = QandA
      fields = ['heading','question','type','img']
      template_name = 'uProfile/qanda_form.html'


      #
      #       if form.is_valid():
      #             return HttpResponseRedirect('/uProfile/')
      # def form_valid(self, form):
      #       form.save()
      #       response = super(QuestionAdd, self).form_valid(form)
      #       # do something with self.object
      #       return response

class Headings(generic.ListView):
      template_name = 'uProfile/ques.html'
      model = QandA
      context_object_name = 'QandA_list'

      def get_queryset(self):
            return QandA.objects.all()

def no(request):
      if request.method == 'POST':
            cursor.execute('''insert into test values(50)''')
            transaction.commit()
            return redirect('uProfile:Qtn')

def help(request):
      if request.method == 'GET':
            search = request.GET['query']
            row = QandA.objects.raw("""Select * from QandA where qHead like %s""" ,('%'+search+'%',))
            userdetail = row
            context = {'QandA_list': userdetail}

            return render(request, 'uProfile/ques.html', context)
class Quesinfo(generic.DetailView):
      template_name = 'uProfile/test.html'
      model = QandA
      context_object_name = 'QandA'

      def get_queryset(self):
            return QandA.objects.all()

      def get(self,request):
            if 'search' in request.GET:
                  row = QandA.objects.raw('Select * from QandA ')
                  userdetail = row
                  context = {'userdetail': userdetail}
                  return render(request, 'uProfile/index.html', context)

class UserFormView(View):
      form_class = UserForm
      template_name = 'uProfile/qanda_form.html'

      def get(self,request):
            form = self.form_class(None)
            return render(request,self.template_name,{'form' : form} )

      def post(self,request):
            form = self.form_class(request.POST)

            if form.is_valid():

                  #not saving data creating object
                  user = form.save(commit=False)

                  #cleaned data
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']
                  user.set_password(password)
                  user.save()
                  #checking whether user already exits
                  user = authenticate(username = username, password = password)

                  if user is not None:

                        if user.is_active:
                              login(request,user)
                              return redirect('uProfile:index')

            return render(request,self.template_name,{'form' : form})

def test(request,c_id = 1):
      ques = QandA.objects.raw('Select 1 as id,qHead as head,question as ques from QandA where id = %s', (c_id,))

      if 'subComment' in request.POST:
            cursor.execute('insert into uProfile_comments(Text,Id_id,ques_id,date) values(%s,%s,%s,%s)',(request.POST.get('textComment',''),request.user.id,c_id,dt.now()))
            transaction.commit()
      if 'subReply' in request.POST:
            cursor.execute('insert into uProfile_replies(Text,commentId_id,reply_id,date) values(%s,%s,%s,%s)',
                           (request.POST.get('textReply', ''),request.POST.get('hiddenId',''),request.user.id,dt.now(),))
            transaction.commit()
      row = QandA.objects.raw('Select * from uProfile_profile')
      num = QandA.objects.raw('Select 1 as id,comment from uProfile_comments where ques_Id = %s order by date DESC',(c_id,),)
      list = []
      for n in num:
            ques = QandA.objects.raw('Select 1 as id,qHead as head,question as ques from QandA where id = %s',(c_id,))
            comments = QandA.objects.raw('Select 1 as id,auth_user.username as name,comment,Text,date from uProfile_comments join auth_user on '
                                          'uProfile_comments.Id_id = auth_user.id  where ques_Id = %s and comment = %s ',(c_id,n.comment,))
            replies =  QandA.objects.raw('Select 1 as id,auth_user.username as name,Text,date from uProfile_replies join  auth_user on uProfile_replies.reply_id = auth_user.id  where commentId_id=%s',(n.comment,))
            count =  QandA.objects.raw('Select 1 as id,count(*) as count from uProfile_replies where commentId_id=%s',(n.comment,))
            list.append({'comments':comments,'replies':replies,'count':count[0].count})
      return render(request, 'uProfile/discuss.html', {'heading':ques[0].head,'question':ques[0].ques,'row':row,'list':list,'pk':c_id})


def addComment(request):
      if request.method == 'POST':
            cursor.execute('''insert into test values(50)''')
            transaction.commit()
            return redirect('uProfile:Qtn')


