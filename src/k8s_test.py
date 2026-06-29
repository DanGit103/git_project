from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("SimpleSparkTest") \
        .getOrCreate()

    # Create a small dataset
    data = [(1,), (2,), (3,), (4,), (5,)]
    df = spark.createDataFrame(data, ["number"])

    # Simple transformation
    df2 = df.withColumn("square", df["number"] * df["number"])

    # Show results
    df2.show()

    print("Row count:", df2.count())

    spark.stop()

if __name__ == "__main__":
    main()