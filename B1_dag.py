from airflow.sdk import dag, task


@dag(dag_id="daily_report", schedule=None)
def report_dag():

    @task
    def extract():
        return [1, 2, 3]

    @task
    def total(numbers):
        print(sum(numbers))

    numbers = extract()
    total(numbers)


report_dag()