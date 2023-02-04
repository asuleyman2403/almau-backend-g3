from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    categories_list = [category.to_json() for category in categories]
    return JsonResponse(data=categories_list, status=200, safe=False)


def get_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        return JsonResponse(data=category.to_json(), status=200, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': 'Category not found'}, status=404)


def get_products(request):
    products = Product.objects.all()
    product_list = [product.to_json() for product in products]
    return JsonResponse(data=product_list, status=200, safe=False)


def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        return JsonResponse(data=product.to_json(), status=200, safe=False)
    except Product.DoesNotExist as e:
        return JsonResponse(data={'message': 'Product not found'}, status=404)


def get_category_products(request, pk):
    try:
        category = Category.objects.get(id=pk)
        products = category.product_set.all()
        product_list = [product.to_json() for product in products]
        return JsonResponse(data=product_list, status=200, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': 'Category not found'}, status=404)


def get_product_of_category(request, pk, pk2):
    try:
        category = Category.objects.get(id=pk)
        try:
            product = category.product_set.get(id=pk2)
            return JsonResponse(data=product.to_json(), status=200, safe=False)
        except Product.DoesNotExist as e:
            return JsonResponse(data={'message': 'Category {} does not have product with ID {}'.format(category.name, pk2)},
                                status=404)
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': 'Category not found'}, status=404)
