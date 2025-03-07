from django import template

register = template.Library()

@register.filter(name='br_currency')
def br_currency(value):
    """Formata o valor no padrão brasileiro: R$ 1.000,00."""
    try:
        value = float(value)
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value
