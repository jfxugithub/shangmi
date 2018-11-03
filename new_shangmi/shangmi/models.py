from django.db import models

# Create your models here.
class ShangmiUser(models.Model):
    openid = models.CharField(
        max_length=255,
        verbose_name="openid"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    nick_name = models.CharField(
        verbose_name="昵称",
        null=True,
        max_length=30
    )
    source = models.CharField(
        max_length=30,
        verbose_name="用户来源"
    )


class Balance(models.Model):
    money = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name="余额"
    )
    user = models.OneToOneField(
        ShangmiUser,
        verbose_name="用户"
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="用户余额更新时间"
    )
    class Meta:
        verbose_name = "余额积分表"


class Advertise(models.Model):
    name = models.CharField(
        verbose_name="海报名字",
        max_length=50
    )
    icon = models.CharField(
        max_length=255,
        verbose_name="海报封面"
    )
    affect_time = models.DateField(
        verbose_name="截止日期",
        null=True
    )
    class Meta:
        verbose_name = "海报"


class Store(models.Model):
    name = models.CharField(
        verbose_name="店铺名",
        max_length=40
    )
    address = models.CharField(
        verbose_name="地址",
        max_length=255,
        null=True
    )
    boss = models.ForeignKey(
        ShangmiUser,
        verbose_name="店老板"
    )
    create_time = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否可用"
    )

class GetMoneyLog(models.Model):
    user = models.ForeignKey(
        ShangmiUser,
        verbose_name="用户"
    )
    money = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name="金额"
    )
    create_time = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True
    )
    class Meta:
        verbose_name = "用户提现表"


class Active(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="活动名字"
    )
    icon = models.CharField(
        max_length=255,
        verbose_name="海报封面"
    )
    desc = models.CharField(
        max_length=255,
        verbose_name="活动描述"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否活跃"
    )
    create_time = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True
    )
    give_money = models.IntegerField(
        verbose_name="活动给予积分"
    )

    class Meta:
        verbose_name = "活动表"


class ActiveStoreMap(models.Model):
    active = models.ForeignKey(
        Active,
        verbose_name="活动"
    )
    store = models.ForeignKey(
        Store,
        verbose_name="门店"
    )
    create_time = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True
    )
    class Meta:
        verbose_name = "活动与门店关系表"
        unique_together = ['store', 'active'] #联合约束