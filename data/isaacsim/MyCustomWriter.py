from omni.replicator.core import AnnotatorRegistry, BackendDispatch, Writer, WriterRegistry


class MyCustomWriter(Writer):

    def __init__(

        self,

        output_dir,

        rgb = False,

        semantic_segmentation = False,

    ):

        self.version = "0.0.1"

        self.backend = BackendDispatch({"paths": {"out_dir": output_dir}})

        if rgb:

            self.annotators.append(AnnotatorRegistry.get_annotator("rgb"))

        if semantic_segmentation:

            self.annotators.append(AnnotatorRegistry.get_annotator("semantic_segmentation"))

        self._frame_id = 0


    def write(self, data):

        if "rgb" in data:

            filename = f"rgb_{self._frame_id}.png"

            self.backend.write_image(filename, data["rgb"])

        if "semantic_segmentation" in data:

            filename = f"semantic_segmentation_{self._frame_id}.png"

            self.backend.write_image(filename, data["semantic_segmentation"])

        print(f"Frame {self._frame_id} written to {self.backend.output_dir}")

        self._frame_id += 1


    def on_final_frame(self):

        print(f"Final frame {self._frame_id} reached")

        self._frame_id = 0


WriterRegistry.register(MyCustomWriter)
