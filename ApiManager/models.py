from django.db import models

from ApiManager.managers import UserTypeManager, UserInfoManager, ProjectInfoManager, ModuleInfoManager, \
    TestCaseInfoManager, EnvInfoManager


# Create your models here.


class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class UserType(BaseTable):
    class Meta:
        verbose_name = '用户类型'
        db_table = 'UserType'

    type_name = models.CharField(max_length=20)
    type_desc = models.CharField(max_length=50)
    objects = UserTypeManager()


class UserInfo(BaseTable):
    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    password = models.CharField('密码', max_length=20, null=False)
    email = models.EmailField('邮箱', null=False, unique=True)
    status = models.IntegerField('有效/无效', default=1)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    objects = UserInfoManager()


class ProjectInfo(BaseTable):
    class Meta:
        verbose_name = '项目信息'
        db_table = 'ProjectInfo'

    project_name = models.CharField('项目名称', max_length=50, unique=True, null=False)
    responsible_name = models.CharField('负责人', max_length=20, null=False)
    test_user = models.CharField('测试人员', max_length=100, null=False)
    dev_user = models.CharField('开发人员', max_length=100, null=False)
    publish_app = models.CharField('发布应用', max_length=100, null=False)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)
    objects = ProjectInfoManager()


class ModuleInfo(BaseTable):
    class Meta:
        verbose_name = '模块信息'
        db_table = 'ModuleInfo'

    module_name = models.CharField('模块名称', max_length=50, null=False)
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField('测试负责人', max_length=50, null=False)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)
    objects = ModuleInfoManager()


class TestCaseInfo(BaseTable):
    class Meta:
        verbose_name = '用例信息'
        db_table = 'TestCaseInfo'

    type = models.IntegerField('test/config', default=1)
    name = models.CharField('用例/配置名称', max_length=50, null=False)
    belong_project = models.CharField('所属项目', max_length=50, null=False)
    belong_module = models.ForeignKey(ModuleInfo, on_delete=models.CASCADE)
    include = models.CharField('前置config/test', max_length=1024, null=True)
    author = models.CharField('编写人员', max_length=20, null=False)
    request = models.TextField('请求信息', null=False)

    objects = TestCaseInfoManager()


class TestReports(BaseTable):
    class Meta:
        verbose_name = "测试报告"
        db_table = 'TestReports'

    report_name = models.CharField(max_length=40, null=False)
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    reports = models.TextField()


class EnvInfo(BaseTable):
    class Meta:
        verbose_name = '环境管理'
        db_table = 'EnvInfo'

    env_name = models.CharField(max_length=40, null=False, unique=True)
    base_url = models.CharField(max_length=40, null=False)
    simple_desc = models.CharField(max_length=50, null=False)
    objects = EnvInfoManager()


class DebugTalk(BaseTable):
    class Meta:
        verbose_name = '驱动py文件'
        db_table = 'DebugTalk'

    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    debugtalk = models.TextField(null=True, default='#debugtalk.py')


class TestSuite(BaseTable):
    class Meta:
        verbose_name = '用例集合'
        db_table = 'TestSuite'

    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    suite_name = models.CharField(max_length=100, null=False)
    include = models.TextField(null=False)


class XmindCase(BaseTable):
    class Meta:
        verbose_name = 'Xmind用例'
        db_table = 'XmindCases'

    '''test case json example
    {
        "module": "子模块1",
        "name": "用例1",
        "version": 1,
        "summary": "用例1",
        "preconditions": "无",
        "execution_type": 1,
        "importance": 2,
        "estimated_exec_duration": 3,
        "status": 7,
        "result": 0,
        "steps": [
            {
                "step_number": 1,
                "actions": "步骤1",
                "expectedresults": "预期1",
                "execution_type": 1,
                "result": 0
            },
            {
                "step_number": 2,
                "actions": "步骤2",
                "expectedresults": "预期2",
                "execution_type": 1,
                "result": 0
            }
        ],
        "product": "6级用例",
        "suite": "模块A"
    }
    '''

    # 用例标题
    name = models.CharField(max_length=256, null=False)
    # 项目名称
    belong_project = models.CharField('所属项目', max_length=50, null=False)
    # 功能模块
    suite = models.CharField('所属模块', max_length=100, null=False)
    # 功能子模块
    belong_module = models.CharField('功能子模块', max_length=100, null=False)
    # 步骤预期
    steps = models.TextField('步骤')
    # 属性
    attributes = models.CharField('属性', max_length=100)
    # 预期
    # expectResult = models.CharField('预期', max_length=256)
    # 用户
    author = models.IntegerField('创建用户', null=False)
    # xmind文件路径
    # file_locate = models.CharField('xmind文件路径', max_length=256, null=False)
    # file name
    file_name = models.CharField('filename', max_length=256, null=False)
    # xmind
    xmind_file = models.FileField('xmind', max_length=256, null=False)
    # xlsx
    xlsx_file = models.FileField('xlsx', max_length=256, null=False)
    # objects = XmindCaseManager()
