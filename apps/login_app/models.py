# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt
import re
# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['first_name'].strip()) < 3:
            results['errors'].append('First name must be at least 3 characters')
            results['status'] = False
        if len(postData['alias'].strip()) < 2:
            results['errors'].append('Alias must be at least 2 characters')
            results['status'] = False
        if len(postData['last_name'].strip()) < 3:
            results['errors'].append('Last name must be at least 3 characters')
            results['status'] = False
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Invalid email')
            results['status'] = False
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False
        if len(postData['password'].strip()) < 3:
            results['errors'].append('Password must be 5 characters')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append('Passwords must match')
            results['status'] = False
        if postData['password'].isalpha() == True:
            results['errors'].append('Password must contain characters and at least 1 number!')
            results['status'] = False
        if len(postData['birthday']) < 8:
            results['errors'].append('Birthday not valid')
            results['status'] = False
        return results

    def creator(self, postData):
        user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], alias=postData['alias'], email=postData['email'], password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(email = postData['email'])

        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

class User(models.Model):
    first_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
