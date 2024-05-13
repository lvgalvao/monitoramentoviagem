from src.main import ProductCollector

def test_check_product_collector():
    """ Verifica se existe o ProductCollector"""
    product_collector = ProductCollector(product_name="coca")
    assert product_collector != None

def test_get_product():
    """"""
    product_collector = ProductCollector(product_name="coca")
    product_collector.get_product()

def test_product_availability():
    """ Funcionalidade onde você passa o nome do produto e volta a disponibilidade do produto"""
    product_collector = ProductCollector(product_name="coca")
    product_collector.product_availability()
