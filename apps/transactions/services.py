def calculate_summary(transactions):
    income = sum(t.amount for t in transactions if t.type == 'income')
    expense = sum(t.amount for t in transactions if t.type == 'expense')

    return {
        'income': income,
        'expense': expense,
        'balance': income - expense
    }


def generate_insights(transactions):
    insights = []

    expenses = [t for t in transactions if t.type == 'expense']

    total_expense = sum(t.amount for t in expenses)

    if total_expense > 1000:
        insights.append("Seus gastos estão altos este mês.")

    if expenses:
        biggest = max(expenses, key=lambda x: x.amount)
        insights.append(f"Seu maior gasto foi R$ {biggest.amount} em {biggest.category}")

    return insights