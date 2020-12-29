from django.db import models
from taggit.managers import TaggableManager
from django.contrib.sites.models import Site
from config import settings


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=255)
    slug = models.SlugField('英語名', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリーリスト'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    thumbnail = models.ImageField('サムネ', upload_to='images/')
    description = models.CharField('headタグでの説明', max_length=255, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = TaggableManager('タグ', blank=True)
    text = models.TextField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)
    is_public = models.BooleanField('公開する', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '投稿'


class Ability(models.Model):
    name = models.CharField('能力', max_length=255, default='NoSetting')
    image = models.ImageField('アイコン', upload_to='ability_img/')
    value = models.IntegerField('進捗度', default='0')
    description = models.TextField('能力の説明')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '能力'
        verbose_name_plural = 'プログラミング能力'


class SiteDetail(models.Model):
    site = models.OneToOneField(
        Site, verbose_name='Site', on_delete=models.PROTECT)
    name = models.CharField('名前', max_length=255, default='NoSetting')
    greeting = models.TextField('プロフィール紹介、挨拶', default='NoSetting')
    email = models.EmailField(
        'メールアドレス', max_length=255, default='your_mail@gmail.com')
    github = models.CharField('Githubアカウント', max_length=255, blank=True)
    twitter = models.CharField('Twitterアカウント', max_length=255, blank=True)
    google_ad_html = models.TextField('アドセンスHTML', blank=True)
    google_analytics_html = models.TextField('アナリティクスHTML', blank=True)

    def __str__(self):
        return self.name


def create_default_site_detail(sender, **kwargs):
    site = Site.objects.get(pk=settings.SITE_ID)
    SiteDetail.objects.get_or_create(site=site)
