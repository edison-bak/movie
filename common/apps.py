from django.apps import AppConfig


class CommonConfig(AppConfig):
    # 이 앱의 모델에 대한 기본 키가 BigAutoField로 설정된다는 것을 의미
    default_auto_field = 'django.db.models.BigAutoField'
    # name 속성은 Django에게 이 앱의 이름이 'common'임을 알려줍니다. 
    # 이는 Django가 앱을 식별하고 관리하는 데 사용
    name = 'common'
