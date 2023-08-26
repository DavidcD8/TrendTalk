from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class CustomPostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    # Use actual fields of the Post model here
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def post_status(self, obj):
        return obj.status
    post_status.short_description = 'Status'

    def published_date(self, obj):
        return obj.created_on
    published_date.short_description = 'Published On'


@admin.register(Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_body',
                    'related_post', 'comment_date', 'is_approved')
    list_filter = ('is_approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_selected_comments']

    def commenter_name(self, obj):
        return obj.name
    commenter_name.short_description = 'Commenter Name'

    def comment_body(self, obj):
        return obj.body
    comment_body.short_description = 'Comment Body'

    def related_post(self, obj):
        return obj.post
    related_post.short_description = 'Related Post'

    def comment_date(self, obj):
        return obj.created_on
    comment_date.short_description = 'Comment Date'

    def is_approved(self, obj):
        return obj.approved
    is_approved.short_description = 'Approved'

    def approve_selected_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_selected_comments.short_description = 'Approve Selected Comments'
