import numpy as np

class INT8Quantizer:
    """Compresses FP32 tensors to INT8 for efficient migration and storage."""
    def quantize(self, tensor: np.ndarray):
        scale = np.max(np.abs(tensor)) / 127
        quantized = (tensor / scale).astype(np.int8)
        return quantized, scale

    def dequantize(self, quantized: np.ndarray, scale: float):
        return quantized.astype(np.float32) * scale
