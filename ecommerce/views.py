from django.http import HttpResponse
from django.shortcuts import render
from ecommerce.models import *
from django.db.models import Q
# Create your views here.

dateFormat = '%d-%m-%Y %H:%M:%S'

def listProducts(request):
    products = Product.objects.prefetch_related('image_set')
    ans = []
    
    for product in products:
        product_dic = {}
        product_dic['title'] = product.title
        product_dic['description'] = product.description
        product_dic['created_at'] = product.created_at.strftime(dateFormat)
        product_dic['updated_at'] = product.updated_at.strftime(dateFormat)
        product_dic['images'] = list(product.image_set.values_list('source', flat = True))
        ans.append(product_dic)
            
    return HttpResponse(ans)

def listVariants(request):
    variants = Variant.objects.select_related("product", "image")
    ans = []
    
    for variant in variants:
        variant_dic = {}
        variant_dic['title'] = variant.product.title + " " + variant.title
        variant_dic['created_at'] = variant.created_at.strftime(dateFormat)
        variant_dic['updated_at'] = variant.updated_at.strftime(dateFormat)
        variant_dic['available_for_sale'] = variant.available_for_sale
        variant_dic['price'] = variant.price
        variant_dic['images'] = variant.image.imageURL
        ans.append(variant_dic)
        
    return HttpResponse(ans)

def listCollections(request):
    ans = list(Collection.objects.all().values("title", "published", "updated_at"))
    return HttpResponse(ans)

def listCollectionProduct(request, id):
    products = Collection.objects.prefetch_related('products__image_set').get(pk = id).products.all()
    ans = []
    
    for product in products:
        product_dic = {}
        product_dic['title'] = product.title
        product_dic['description'] = product.description
        product_dic['created_at'] = product.created_at.strftime(dateFormat)
        product_dic['updated_at'] = product.updated_at.strftime(dateFormat)
        product_dic['images'] = list([image.source for image in product.image_set.all()])
        ans.append(product_dic)
    
    return HttpResponse(ans)

def listVariantCollection(request, id):
    products = Collection.objects.prefetch_related('products__variant_set__image').get(pk = id).products.all()
    ans = []
    
    for product in products:
        variants = product.variant_set.all()
        
        for variant in variants:
            variant_dic = {}
            variant_dic['title'] = variant.product.title + " " + variant.title
            variant_dic['created_at'] = variant.created_at.strftime(dateFormat)
            variant_dic['updated_at'] = variant.updated_at.strftime(dateFormat)
            variant_dic['available_for_sale'] = variant.available_for_sale
            variant_dic['price'] = variant.price
            variant_dic['images'] = variant.image.imageURL
            ans.append(variant_dic)
    
    return HttpResponse(ans)
    # return ans

def listVariantCategory(request, id):
    c = Category.objects.get(pk = id)
    ans = []
    
    def get_all_subcategories(c):
        result = []

        result.append(c)
        for c in Category.objects.filter(parent=c):
            temp = get_all_subcategories(c)
            if len(temp) > 0:
                result.extend(temp)
        return result
    
    sub_categories = get_all_subcategories(c)
    subcategories = Category.objects.prefetch_related('product_set__variant_set__image').filter(pk__in = [sub.pk for sub in sub_categories])
    
    for subcategory in subcategories:
        products = subcategory.product_set.all()
        
        for product in products:
            variants = product.variant_set.all()
            for variant in variants:
                variant_dic = {}
                variant_dic['title'] = product.title + " " + variant.title
                variant_dic['created_at'] = variant.created_at.strftime(dateFormat)
                variant_dic['updated_at'] = variant.updated_at.strftime(dateFormat)
                variant_dic['available_for_sale'] = variant.available_for_sale
                variant_dic['price'] = variant.price
                variant_dic['images'] = variant.image.imageURL
                ans.append(variant_dic)
    print(ans)
    return HttpResponse(ans)
        
    
    
    
    
    
    # for subcategory in sub_categories:
    #     products = Category.objects.prefetch_related('product_set__variant_set__image').get(pk = subcategory.pk).product_set.all()
    #     print("products, ",products)
    #     # products = subcategory.prefetch_related('product_set__variant_set__image_variant').product_set.all()
        
    #     for product in products:
    #         variants = product.variant_set.all()
    #         for variant in variants:
    #             variant_dic = {}
    #             variant_dic['title'] = variant.product.title + " " + variant.title
    #             variant_dic['created_at'] = variant.created_at.strftime(dateFormat)
    #             variant_dic['updated_at'] = variant.updated_at.strftime(dateFormat)
    #             variant_dic['available_for_sale'] = variant.available_for_sale
    #             variant_dic['price'] = variant.price
    #             variant_dic['images'] = variant.image.imageURL
    #             ans.append(variant_dic)

# def listVariantCategory(request, id):
#     # subcategory = Categories.objects.filter(Q(subcategory__pk = id) | Q(pk = id)).prefetch_related('product_set__variant_set__image_variant').product_set.all()
#     # print("subcategory, ", subcategory)
#     products = Categories.objects.prefetch_related('product_set__variant_set__image_variant').get(pk = id).product_set.all()
#     ans = []
    
#     for product in products:
#         variants = product.variant_set.all()
#         for variant in variants:
#             variant_dic = {}
#             variant_dic['title'] = variant.product_variant.title + " " + variant.title
#             variant_dic['created_at'] = variant.created_at.strftime(dateFormat)
#             variant_dic['updated_at'] = variant.updated_at.strftime(dateFormat)
#             variant_dic['available_for_sale'] = variant.available_for_sale
#             variant_dic['price'] = variant.price
#             variant_dic['images'] = variant.image_variant.imageURL
#             ans.append(variant_dic)
    
    
#     return HttpResponse(ans)
    
    


    
    
    
    