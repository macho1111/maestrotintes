from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Apparel, Material, ConsentText


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
        
        # アパレルとマテリアルから Product インスタンスを作成して保存
        product = Product.objects.create(
            apparel=apparel,
            material=material
        )
        if image:
            # Product インスタンスに画像を関連付けて保存
            product.image = image
            product.save()
        return redirect('product_list')  # 注文が完了したらアイテムリストページにリダイレクトする
    return redirect('product_list')  # POSTリクエスト以外はアイテムリストページにリダイレクトする

def product_list(request):
    products = Product.objects.all()
    return render(request, 'maruko/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'maruko/product_detail.html', {'product': product})

def consent_view(request):
    # ConsentTextモデルからすべての同意書の内容を取得
    consent_texts = ConsentText.objects.all()
    return render(request, 'maruko/consent_template.html', {'consent_texts': consent_texts})