# apply_quantisation.py

import torch
from torch.quantization import quantize_dynamic, prepare_qat, convert
from models import PolicyNetwork

# Apply Post-Training Quantization (PTQ)
def apply_ptq(policy):
    """
    Apply Post-Training Quantization to the model.
    """
    torch.backends.quantized.engine = 'qnnpack'
    quantised_policy = quantize_dynamic(policy, {torch.nn.Linear}, dtype=torch.qint8)
    return quantised_policy

# Apply Quantization-Aware Training (QAT)
def apply_qat(policy, calibration_data):
    """
    Apply Quantization-Aware Training to the model.
    """
    policy.qconfig = torch.quantization.get_default_qconfig('qnnpack')
    prepare_qat(policy, inplace=True)

    # Calibrate the model with representative input data
    print("Calibrating QAT model...")
    with torch.no_grad():
        for data in calibration_data:
            policy(data)

    # Convert the model to quantized form
    print("Converting QAT model...")
    quantised_policy = convert(policy, inplace=False)

    return quantised_policy

if __name__ == "__main__":
    input_dim = 4  # CartPole observation space
    output_dim = 2  # CartPole action space

    # Load the trained policy
    print("Loading baseline policy...")
    policy = PolicyNetwork(input_dim, output_dim)
    policy.load_state_dict(torch.load("./models/policy.pth"))
    print("Baseline policy loaded.")

    # Generate dummy calibration data for demonstration
    calibration_data = [torch.rand(1, input_dim) for _ in range(100)]

    # Apply PTQ
    print("Applying PTQ...")
    ptq_policy = apply_ptq(policy)
    torch.save(ptq_policy.state_dict(), "./models/ptq_policy.pth")
    print("PTQ model saved to './models/ptq_policy.pth'.")

    # Apply QAT
    print("Applying QAT...")
    qat_policy = apply_qat(policy, calibration_data)
    torch.save(qat_policy.state_dict(), "./models/qat_policy.pth")
    print("QAT model saved to './models/qat_policy.pth'.")
