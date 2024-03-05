from django.apps import AppConfig

class ApkDownloaderConfig(AppConfig):
    name = 'apk_downloader'
    verbose_name = 'APK Downloader'

    def ready(self):
        # Import any signals or other app-specific startup activities here
        pass
