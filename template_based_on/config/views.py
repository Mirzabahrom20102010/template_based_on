from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from posts.models import Post

def home_view(request):
    latest_posts = Post.objects.order_by('-created_at')[:10]
    most_viewed_posts = Post.objects.order_by('-views')[:10]
    week_ago = timezone.now() - timedelta(days=7)
    popular_week_posts = Post.objects.filter(created_at__gte=week_ago).order_by('-views')[:10]
    month_ago = timezone.now() - timedelta(days=30)
    popular_month_posts = Post.objects.filter(created_at__gte=month_ago).order_by('-views')[:10]
    recommended_posts = Post.objects.filter(is_recommended=True)[:10]
    context = {
        'last_posts': latest_posts,
        'popular_posts': most_viewed_posts,
        'week_posts': popular_week_posts,
        'month_posts': popular_month_posts,
        'recommended_posts': recommended_posts,
    }
    return render(request, 'home_page.html', context)