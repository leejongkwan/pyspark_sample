
import ingest
import transform
import persist

class Pipeline:

    def run_pipeline(self):
        print("Running Pipeline")
        ingest_process = ingest.Ingest()
        ingest_process.ingest_data()
        tranform_process = transform.Transform()
        tranform_process.transform_data()
        persist_process = persist.Persist()
        persist_process.persist_data()

if __name__ == '__main__':
    pipeline = Pipeline()
    pipeline.run_pipeline()

