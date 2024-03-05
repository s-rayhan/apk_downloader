from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Apk
from .forms import ApkForm

def index(request):
    apks = Apk.objects.all()
    return render(request, 'apk_downloader/index.html', {'apks': apks})

def upload_apk(request):
    if request.method == 'POST':
        form = ApkForm(request.POST, request.FILES)
        if form.is_valid():
            apk = form.save()
            return redirect('index')
    else:
        form = ApkForm()
    return render(request, 'apk_downloader/upload.html', {'form': form})

def download_apk(request, apk_id):
    try:
        apk = Apk.objects.get(pk=apk_id)
        apk_file = apk.file
        response = HttpResponse(apk_file.read(), content_type='application/vnd.android.package-archive')
        response['Content-Disposition'] = f'attachment; filename="{apk.name}"'
        apk.downloads += 1
        apk.save()
        # Optional success message (add in templates/apk_downloader/download.html if desired)
        # context = {'success_message': f'Download successful! Downloaded {apk.downloads} times.'}
        # return render(request, 'apk_downloader/download.html', context)  # Uncomment if using download.html
        return response
    except Apk.DoesNotExist:
        return render(request, 'apk_downloader/apk_not_found.html')
