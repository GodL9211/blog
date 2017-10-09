from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)

#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

#文章
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateField()
    #文章最后修改时间
    modified_time = models.DateField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    #文章阅读量
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])