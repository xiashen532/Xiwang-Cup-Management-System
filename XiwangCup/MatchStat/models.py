from django.db import models


# Create your models here.

class Team(models.Model):
    team_name = models.CharField('队伍名', max_length=50)  # 队伍名
    group = models.CharField('小组', max_length=100)  # 小组名
    points = models.IntegerField('积分', default=0)  # 积分
    win = models.IntegerField('胜场', default=0)  # 胜场
    draw = models.IntegerField('平场', default=0)  # 平场
    lost = models.IntegerField('负场', default=0)  # 负场
    logo_url = models.CharField('logourl', default='../static/images/fa', max_length=9999)  # logourl

    class Meta:
        verbose_name_plural = '队伍表'

    def __str__(self):
        return self.team_name


class Player(models.Model):
    # 运动员模型
    player_name = models.CharField('运动员', max_length=30)  # 运动员名字
    goal = models.IntegerField('进球', default=0)  # 总进球数
    y_card = models.IntegerField('黄牌', default=0)  # 黄牌数
    r_card = models.IntegerField('红牌', default=0)  # 红牌数
    photo_url = models.CharField('照片url', default='../static/images/defaultphoto.png', max_length=9999)  # 照片url

    player_team = models.ForeignKey(Team,
                                    related_name='players',
                                    on_delete=models.CASCADE,
                                    verbose_name='队伍')  # 定义外键，Team和Player是1:n

    class Meta:
        ordering = ['-goal']  # 按照进球数降序排序
        verbose_name_plural = '队员表'

    def __str__(self):
        return self.player_name


class Match(models.Model):
    match_no = models.IntegerField('比赛编号', default=0)  # 比赛序号
    h_team_name = models.ForeignKey(Team,
                                    related_name='h_team',
                                    on_delete=models.CASCADE,
                                    verbose_name='主队')  # 主队
    a_team_name = models.ForeignKey(Team,
                                    related_name='a_team',
                                    on_delete=models.CASCADE,
                                    verbose_name='客队')  # 客队

    h_score = models.IntegerField('主队进球', default=0)  # 主队进球数
    a_score = models.IntegerField('客队进球', default=0)  # 客队进球数

    match_time = models.DateTimeField('比赛时间')  # 比赛时间
    match_loc = models.CharField('比赛地点', max_length=50)  # 比赛地点

    class Meta:
        verbose_name_plural = '比赛表'

    def __str__(self):
        return str(self.match_no)
