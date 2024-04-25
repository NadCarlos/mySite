import logging
from typing import List, Optional

from products.models import (
    Product,
    Category,
)


#logger = logging.getLogger(__name__)

class ProductRepository:

    def get_all(self) -> List[Product]:
        #logger.info('Se estan obteniendo los producto, aguarde porfavor')
        return Product.objects.all()


    def filter_by_id(self, id: int) -> Optional[Product]:
        return Product.objects.filter(id=id).first()
    

    def get_by_id(self, id: int) -> Optional[Product]:
        try:
            product =  Product.objects.get(id=id)
        except:
            product = None
        return product

    def get_product_on_price_range(
        self, 
        min_price: float, 
        max_price: float
    ) -> List[Product]:
        products = Product.objects.filter(
            price__range=(min_price, max_price)
        )

        return products


    def create(
        self, 
        name: str, 
        price: float,
        description: Optional[str] = None,
        stock: Optional[int] = 0,
        category: Optional[Category] = None
    ):
        return Product.objects.create(
            name = name,
            price = price,
            description = description,
            stock = stock,
            category = category,
        )


    def filter_by_category(
        self,
        category: Category,
    ) -> List[Product]:
        return Product.objects.filter(category=category)


    def filter_by_category_name(
        self,
        nombre_categoria: str,
    ) -> List[Product]:
        return Product.objects.filter(
            category__name=nombre_categoria
        )

    def detele(self, producto: Product):
        return producto.delete()    

    #Similares a get_product_on_price_range()
    def get_product_gte_stock():
        ...


    def get_product_lte_stock():
        ...