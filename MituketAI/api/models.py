from django.db import models
import uuid


class Item(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100,blank=True)
    time = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(upload_to='',blank=True,null=True)
    color = models.CharField(max_length=100,blank=True)
    size = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return 'id:' + str(self.id) + ', name:' + self.name + ', place:' + self.place + ', time:' + str(self.time) + ', image:' + str(self.image) + ', color:' + self.color + ', size:' + self.size
    
class Register(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254,unique=True)
    point = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return 'id:' + str(self.id) + ', name:' + self.name + ', mail:' + self.mail + ', point:' + str(self.point)

class Result(models.Model):
    count = models.PositiveSmallIntegerField(default=0)
    avg = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        # アカウントの数を取得
        self.count = Register.objects.count()
        
        # アカウント全体のポイントの平均を計算
        total_points = Register.objects.aggregate(models.Sum('points'))['points__sum']
        
        if self.count > 0:
            self.avg = total_points // self.count  # 整数での平均を計算
        else:
            self.avg = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f'count: {self.count}, avg: {self.avg}'

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
