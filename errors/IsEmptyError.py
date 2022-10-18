class IsEmptyError(Exception):
  def __init__(self) -> None:
    super().__init__('Entrada inválida. O valor não pode ser vazio.')