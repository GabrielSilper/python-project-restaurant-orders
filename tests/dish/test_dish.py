from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import restriction_map  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    lasagna = "Lasagna"
    camarao = "Camarão passado na manteiga"
    price1 = 45
    price2 = 78
    mussarela1 = Ingredient("queijo mussarela")
    lasagna_recipe1 = Dish(lasagna, price1)
    lasagna_recipe2 = Dish(lasagna, price1)
    camarao_recipe = Dish(camarao, price2)
    restriction_set = restriction_map().get("queijo mussarela")

    # 2.1 - Será validado que seu teste falha caso o atributo name de um prato
    # seja diferente que o passado ao construtor.
    assert lasagna_recipe1.name == lasagna

    # 2.2 - Será validado que seu teste falha caso os hashes de dois pratos
    # iguais sejam diferentes;
    assert (hash(lasagna_recipe1) == hash(lasagna_recipe2)) is True

    # 2.3 - Será validado que seu teste falha caso os hashes de dois pratos
    # diferentes sejam iguais;
    assert (hash(lasagna_recipe1) == hash(camarao_recipe)) is False

    # 2.4 - Será validado que seu teste falha caso a comparação de igualdade de
    # dois pratos iguais (ou de um prato com ele mesmo) seja falsa;
    assert (lasagna_recipe1 == lasagna_recipe2) is True

    # 2.6 - Será validado que seu teste falha caso a implementação do método
    # __repr__ retorne um valor inadequado;
    assert lasagna_recipe2.__repr__() == f"Dish('{lasagna}', R${price1:.2f})"

    # 2.7 - Será validado que seu teste falha caso um TypeError não seja
    # levantado ao criar um prato com um valor de tipo inválido;
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Prato teste", "Cem reais")

    # 2.8 - Será validado que seu teste falha caso um ValueError não seja
    # levantado ao criar um prato com um valor inválido;
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Prato teste", -100)

    # 2.9 - Será validado que seu teste falha caso o acesso a um valor do
    # atributo recipe, ao ser indexado com um ingrediente válido retorne uma
    # quantidade inválida (dica: use o método get do dicionário,
    # por exemplo dish.recipe.get(ingredient));
    lasagna_recipe1.add_ingredient_dependency(mussarela1, 2)
    assert lasagna_recipe1.recipe.get(mussarela1) == 2

    # 2.10 - Será validado que seu teste falha caso o método get_restrictions
    # retorne um set de restrições diferente do esperado;
    assert lasagna_recipe1.get_restrictions() == restriction_set

    # Será validado que seu teste falha caso o método get_ingredients retorne
    # um set de ingredientes diferente do esperado;
    assert lasagna_recipe1.get_ingredients() == {mussarela1}
