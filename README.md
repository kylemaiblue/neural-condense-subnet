<div align="center">
<picture>
    <source srcset="./assets/images/condense-main.png">
    <img src="./assets/images/condense-main.png" alt="Neural Condense Subnet" style="width:800px;">

</picture>
</div>

<div align="center">

# ⚡ 

</div>


## 🌟 Key Features:

### ⚡ Subnet as an Accelerate Adapter for LLM Inference
- 🌐 **Seamless Integration**: Effortlessly integrates with LLM inference engines, such as transformers 🤗, vllm.
- 🧩 **Token Compression**: The subnet API compresses long sequences of natural language tokens into soft tokens.
- 🏛️ **Decentralized Network**: The subnet is a decentralized network that allows miners to contribute to the compression process.
- 📊 **Tiered System**: The subnet has a tiered system, with a research tier for experimentation and an inference tier for production-scale use.
- 📏 **Benchmarking and Validation**: The subnet owner defines synthetic metrics to benchmark miners’ performance, ensuring quality and efficiency.

### ⚙️ Node Tiers


| **Tier**       | **Purpose**                           | **Context Size**         | **Speed**     | **Supporting Models**               |
|----------------|---------------------------------------|---------------------------|---------------|--------------------------------------|
| `research`     | Warmup tier for new LLM model releases | Flexible                  | Unrestricted  | `mistralai/Mistral-7B-Instruct-v0.2` |
| `inference_0`  | Optimized for **long context** in popular LLMs | Up to 1536 tokens       | Fast         | `mistralai/Mistral-7B-Instruct-v0.2` |
| `inference_1`  | Optimized for **very long context** in popular LLMs | Up to 4096 tokens       | Fast         | `mistralai/Mistral-7B-Instruct-v0.2` |

*Supporting models can be flexibly added based on tailored need.*


--- 


### 🔒 Subnet as a Data Encryption Layer for Bittensor
- **Neural Encrypted Conversations:** The subnet offers an additional benefit regarding privacy. If users or companies utilize a subnet to transform their context into condensed tokens before sending them to other LLM services, this approach can help prevent context leaks. The transformation increases the computational complexity, making it more difficult for unauthorized entities to extract the original context.


## 📚 Documentation
- **Setup for miners**: [Miner Setup](./docs/miner.md)
- **Setup for validators**: [Validator Setup](./docs/validator.md)
