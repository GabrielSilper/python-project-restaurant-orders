from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import restriction_map


# Req 1
def test_ingredient():
    # instancia de ingredientes que vou usar nos testes.
    ingredient_name = "queijo mussarela"
    mussarela1 = Ingredient("queijo mussarela")
    mussarela2 = Ingredient("queijo mussarela")
    provolone = Ingredient("queijo provolone")
    restriction_list = restriction_map().get("queijo mussarela", set())

    # 1.1 - Será validado que seu teste falha caso a classe
    # retorne hashes diferentes para dois ingredientes iguais;
    assert hash(mussarela1) == hash(mussarela2)

    # 1.2 - Será validado que seu teste falha caso a classe retorne
    # hashes iguais para dois ingredientes diferentes;
    assert hash(mussarela1) != hash(provolone)

    # 1.3 - Será validado que seu teste falha caso a comparação de igualdade de
    # dois ingredientes iguais (ou de um ingrediente com ele mesmo) seja falsa;
    assert (mussarela1 == mussarela1) is True
    assert (mussarela1 == mussarela2) is True

    # 1.5 - Será validado que seu teste falha
    # caso a implementação do método __repr__ retorne um valor inadequado.
    # captured = capsys.readouterr()
    # print(mussarela1)
    # assert captured.out == "Ingredient('queijo mussarela')"
    assert mussarela1.__repr__() == "Ingredient('queijo mussarela')"

    # 1.6 - Será validado que seu teste falha caso o atributo
    # name de um ingrediente seja diferente que o passado ao construtor.
    assert mussarela1.name == ingredient_name

    # 1.7-Será validado que seu teste falha caso o atributo restrictions de um
    # ingrediente não contenha os valores corretos para o alimento passado.
    assert mussarela1.restrictions == restriction_list
