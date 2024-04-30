from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username = "testuser",
            email = "testuser@gmail.com",
            password = "secrete")

        

        self.post = Post.objects.create(
            title = "This is a good title",
            body = "Nice body content",
            author = self.user

        )
    def test_string_representation(self):
        post = Post(title= "A sample title")
        self.assertEqual(str(post),post.title)   

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','This is a good title')  
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','Nice body content')

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_respose = self.client.get('/post/100000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_respose.status_code,404)
        self.assertContains(response,'This is a good title')
        self.assertTemplateUsed(response,'post_detail.html')

    def test_create_post_create_view(self):
        response = self.client.post(reverse('post_new'),
                                            {'title':'New title',
                                             'body':'new text',
                                             'author':self.user.id
                                             })   
        self.assertEqual(response.status_code,302) 
        self.assertEqual(Post.objects.last().title,'New title')
        self.assertEqual(Post.objects.last().body,'new text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit',args='1')  ,{
                                                                     'title': 'Updated title',
                                                                     'body': 'Updated body'
        })
        self.assertEqual(response.status_code,302)

    def test_delete_view(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code,302) 



       
