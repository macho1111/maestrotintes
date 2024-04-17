from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Apparel, Material, ConsentText
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

def howto(request):
    return render(request, 'maruko/howto.html')

def product_comp(request):
    return render(request, 'maruko/product_comp.html')

def apparel_list(request):
    apparels = Apparel.objects.all()
    return render(request, 'maruko/apparel_list.html', {'apparels': apparels})

def apparel_detail(request, apparel_id):
    apparel = get_object_or_404(Apparel, pk=apparel_id)
    materials = Material.objects.all()
    context = {
        'apparel': apparel,
        'materials': materials,
    }
    return render(request, 'maruko/apparel_detail.html', context)

def create_product(request):
    if request.method == 'POST':
        apparel_id = request.POST.get('apparel_id')
        material_id = request.POST.get('material_id')
        image = request.FILES.get('image')  # アップロードされた画像
        
        # アパレルとマテリアルのインスタンスを取得
        apparel = get_object_or_404(Apparel, pk=apparel_id)
        material = get_object_or_404(Material, pk=material_id)
        
        # ログインユーザーを取得
        user = request.user
        
        # アパレルとマテリアルから Product インスタンスを作成して保存
        product = Product.objects.create(
            apparel=apparel,
            material=material,
            user=user  # ログインユーザーを関連付ける
        )
        if image:
            # Product インスタンスに画像を関連付けて保存
            product.image = image
            product.save()
        return redirect('product_comp')  # 注文が完了したらアイテムリストページにリダイレクトする
    return redirect('product_comp')  # POSTリクエスト以外はアイテムリストページにリダイレクトする
    
class OwnerOnly(UserPassesTestMixin):
    def test_func(self):
        # Check if there are any products in the queryset
        if self.get_queryset().exists():
            # Get the first product in the queryset
            product = self.get_queryset().first()
            # Check if the product's user attribute matches the request user
            return product.user == self.request.user
        else:
            # If there are no products, return False
            return redirect('consent_view') 
    

class ProductListView(OwnerOnly, ListView):
    model = Product
    template_name = 'maruko/product_list.html'
    context_object_name = 'products'
    
    def dispatch(self, request, *args, **kwargs):
        # ログインしていない場合はログインページにリダイレクト
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()  # スタッフの場合はすべての製品を返す
        else:
            return super().get_queryset().filter(user=self.request.user)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'maruko/product_detail.html'
    context_object_name = 'product'

class ConsentView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        # ログインしていない場合はログインページにリダイレクト
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # ConsentTextモデルからすべての同意書の内容を取得
        consent_texts = ConsentText.objects.all()
        return render(request, 'maruko/consent_template.html', {'consent_texts': consent_texts})