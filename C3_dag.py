from airflow.decorators import dag, task
from datetime import datetime


@dag(
    dag_id="stock_check",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
def stock_check():

    @task
    def check_stock():
        return {"item": "rice", "qty": 12}

    @task.branch
    def decide(stock):
        if stock["qty"] < 20:
            return "place_order"
        return "skip_order"

    @task.bash
    def place_order():
        return 'echo "Placing order for rice"'

    @task.bash
    def skip_order():
        return 'echo "No order needed"'

    @task
    def notify():
        print("stock check done")

    stock = check_stock()
    decision = decide(stock)

    decision >> [place_order(), skip_order()]
    [place_order(), skip_order()] >> notify()


stock_check()


#the dag diagram is visible on airflow ui