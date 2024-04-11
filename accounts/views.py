from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import User

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'furigana', 'address', 'phone_number']  # 編集可能なフィールドを指定
    template_name = 'accounts/profile_edit.html'  # ユーザー情報編集ページのテンプレート
    success_url = reverse_lazy('profile_edit')  # 編集が成功した場合のリダイレクト先

    def get_object(self, queryset=None):
        return self.request.user  # ログインユーザーの情報を取得