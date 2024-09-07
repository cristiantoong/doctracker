from django.shortcuts import render, redirect
from photos.forms import PhotoForm
from photos.models import Photo
from django.contrib.auth.decorators import login_required

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_gallery')
    else:
        form = PhotoForm()
    return render(request, 'photos/post/upload_photo.html', {'form': form})

def photo_gallery(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photos/post/gallery.html', {'photos': photos})
