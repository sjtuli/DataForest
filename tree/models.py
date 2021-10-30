from django.db import models
from QuestionApp.models import Question
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import markdown,time
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField #必须导入
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=128, unique=False, verbose_name='名称')
#    parent = models.ForeignKey('self', on_delete=models.PROTECT, db_constraint=False,
#                               null=True, blank=True, verbose_name='父部门')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, db_constraint=False,
                               null=True, blank=True, verbose_name='父部门')
    question = models.ForeignKey('QuestionApp.Question',related_name='department', on_delete=models.CASCADE, null=True, default=3, verbose_name='关联实验')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '树'
        verbose_name_plural = verbose_name #复数形式


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


def get_file_upload_path(instance, filename):
    # return '{username}/cover/{date}/{filename}'.format(username=instance.author.username,date=time.strftime('%Y/%m/%d', time.localtime()),filename=filename)
    return '{department}/{filename}'.format(department=instance.department_id, filename=filename)


class Node(models.Model):
    author = models.ForeignKey(User, related_name='nodes', verbose_name='回答者', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='节点', related_name='node', on_delete=models.CASCADE)
    # body = models.TextField('正文', default='')
    body =MDTextField('正文', default='')
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    def __str__(self):
        return str(self.department_id)
    class Meta:
        verbose_name = '节点'
        verbose_name_plural = verbose_name
    def save(self,*args,**kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args,**kwargs)
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数



class NodeFile(models.Model):
    File = models.FileField('文件路径', null=True, upload_to=get_file_upload_path, default='')
    File_name = models.CharField('文件名', null=True, default='', max_length=128)
    node = models.ForeignKey('Node', related_name="file", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='节点', null=True, default='', related_name='file', on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.File_name)