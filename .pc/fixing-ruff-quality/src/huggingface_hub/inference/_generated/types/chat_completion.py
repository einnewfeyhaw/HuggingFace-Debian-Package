# Inference code generated from the JSON schema spec in @huggingface/tasks.
#
# See:
#   - script: https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/scripts/inference-codegen.ts
#   - specs:  https://github.com/huggingface/huggingface.js/tree/main/packages/tasks/src/tasks.
from typing import Any, List, Literal, Optional, Union

from .base import BaseInferenceType, dataclass_with_extra


@dataclass_with_extra
class ChatCompletionInputURL(BaseInferenceType):
    url: str


ChatCompletionInputMessageChunkType = Literal["text", "image_url"]


@dataclass_with_extra
class ChatCompletionInputMessageChunk(BaseInferenceType):
    type: "ChatCompletionInputMessageChunkType"
    image_url: Optional[ChatCompletionInputURL] = None
    text: Optional[str] = None


@dataclass_with_extra
class ChatCompletionInputMessage(BaseInferenceType):
    content: Union[List[ChatCompletionInputMessageChunk], str]
    role: str
    name: Optional[str] = None


ChatCompletionInputGrammarTypeType = Literal["json", "regex"]


@dataclass_with_extra
class ChatCompletionInputGrammarType(BaseInferenceType):
    type: "ChatCompletionInputGrammarTypeType"
    value: Any
    """A string that represents a [JSON Schema](https://json-schema.org/).
    JSON Schema is a declarative language that allows to annotate JSON documents
    with types and descriptions.
    """


@dataclass_with_extra
class ChatCompletionInputStreamOptions(BaseInferenceType):
    include_usage: bool
    """If set, an additional chunk will be streamed before the data: [DONE] message. The usage
    field on this chunk shows the token usage statistics for the entire request, and the
    choices field will always be an empty array. All other chunks will also include a usage
    field, but with a null value.
    """


@dataclass_with_extra
class ChatCompletionInputFunctionName(BaseInferenceType):
    name: str


@dataclass_with_extra
class ChatCompletionInputToolChoiceClass(BaseInferenceType):
    function: ChatCompletionInputFunctionName


ChatCompletionInputToolChoiceEnum = Literal["auto", "none", "required"]


@dataclass_with_extra
class ChatCompletionInputFunctionDefinition(BaseInferenceType):
    arguments: Any
    name: str
    description: Optional[str] = None


@dataclass_with_extra
class ChatCompletionInputTool(BaseInferenceType):
    function: ChatCompletionInputFunctionDefinition
    type: str


@dataclass_with_extra
class ChatCompletionInput(BaseInferenceType):
    """Chat Completion Input.
    Auto-generated from TGI specs.
    For more details, check out
    https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/scripts/inference-tgi-import.ts.
    """

    messages: List[ChatCompletionInputMessage]
    """A list of messages comprising the conversation so far."""
    frequency_penalty: Optional[float] = None
    """Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing
    frequency in the text so far,
    decreasing the model's likelihood to repeat the same line verbatim.
    """
    logit_bias: Optional[List[float]] = None
    """UNUSED
    Modify the likelihood of specified tokens appearing in the completion. Accepts a JSON
    object that maps tokens
    (specified by their token ID in the tokenizer) to an associated bias value from -100 to
    100. Mathematically,
    the bias is added to the logits generated by the model prior to sampling. The exact
    effect will vary per model,
    but values between -1 and 1 should decrease or increase likelihood of selection; values
    like -100 or 100 should
    result in a ban or exclusive selection of the relevant token.
    """
    logprobs: Optional[bool] = None
    """Whether to return log probabilities of the output tokens or not. If true, returns the log
    probabilities of each
    output token returned in the content of message.
    """
    max_tokens: Optional[int] = None
    """The maximum number of tokens that can be generated in the chat completion."""
    model: Optional[str] = None
    """[UNUSED] ID of the model to use. See the model endpoint compatibility table for details
    on which models work with the Chat API.
    """
    n: Optional[int] = None
    """UNUSED
    How many chat completion choices to generate for each input message. Note that you will
    be charged based on the
    number of generated tokens across all of the choices. Keep n as 1 to minimize costs.
    """
    presence_penalty: Optional[float] = None
    """Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they
    appear in the text so far,
    increasing the model's likelihood to talk about new topics
    """
    response_format: Optional[ChatCompletionInputGrammarType] = None
    seed: Optional[int] = None
    stop: Optional[List[str]] = None
    """Up to 4 sequences where the API will stop generating further tokens."""
    stream: Optional[bool] = None
    stream_options: Optional[ChatCompletionInputStreamOptions] = None
    temperature: Optional[float] = None
    """What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the
    output more random, while
    lower values like 0.2 will make it more focused and deterministic.
    We generally recommend altering this or `top_p` but not both.
    """
    tool_choice: Optional[
        Union[ChatCompletionInputToolChoiceClass, "ChatCompletionInputToolChoiceEnum"]
    ] = None
    tool_prompt: Optional[str] = None
    """A prompt to be appended before the tools"""
    tools: Optional[List[ChatCompletionInputTool]] = None
    """A list of tools the model may call. Currently, only functions are supported as a tool.
    Use this to provide a list of
    functions the model may generate JSON inputs for.
    """
    top_logprobs: Optional[int] = None
    """An integer between 0 and 5 specifying the number of most likely tokens to return at each
    token position, each with
    an associated log probability. logprobs must be set to true if this parameter is used.
    """
    top_p: Optional[float] = None
    """An alternative to sampling with temperature, called nucleus sampling, where the model
    considers the results of the
    tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10%
    probability mass are considered.
    """


@dataclass_with_extra
class ChatCompletionOutputTopLogprob(BaseInferenceType):
    logprob: float
    token: str


@dataclass_with_extra
class ChatCompletionOutputLogprob(BaseInferenceType):
    logprob: float
    token: str
    top_logprobs: List[ChatCompletionOutputTopLogprob]


@dataclass_with_extra
class ChatCompletionOutputLogprobs(BaseInferenceType):
    content: List[ChatCompletionOutputLogprob]


@dataclass_with_extra
class ChatCompletionOutputFunctionDefinition(BaseInferenceType):
    arguments: Any
    name: str
    description: Optional[str] = None


@dataclass_with_extra
class ChatCompletionOutputToolCall(BaseInferenceType):
    function: ChatCompletionOutputFunctionDefinition
    id: str
    type: str


@dataclass_with_extra
class ChatCompletionOutputMessage(BaseInferenceType):
    role: str
    content: Optional[str] = None
    tool_calls: Optional[List[ChatCompletionOutputToolCall]] = None


@dataclass_with_extra
class ChatCompletionOutputComplete(BaseInferenceType):
    finish_reason: str
    index: int
    message: ChatCompletionOutputMessage
    logprobs: Optional[ChatCompletionOutputLogprobs] = None


@dataclass_with_extra
class ChatCompletionOutputUsage(BaseInferenceType):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


@dataclass_with_extra
class ChatCompletionOutput(BaseInferenceType):
    """Chat Completion Output.
    Auto-generated from TGI specs.
    For more details, check out
    https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/scripts/inference-tgi-import.ts.
    """

    choices: List[ChatCompletionOutputComplete]
    created: int
    id: str
    model: str
    system_fingerprint: str
    usage: ChatCompletionOutputUsage


@dataclass_with_extra
class ChatCompletionStreamOutputFunction(BaseInferenceType):
    arguments: str
    name: Optional[str] = None


@dataclass_with_extra
class ChatCompletionStreamOutputDeltaToolCall(BaseInferenceType):
    function: ChatCompletionStreamOutputFunction
    id: str
    index: int
    type: str


@dataclass_with_extra
class ChatCompletionStreamOutputDelta(BaseInferenceType):
    role: str
    content: Optional[str] = None
    tool_calls: Optional[ChatCompletionStreamOutputDeltaToolCall] = None


@dataclass_with_extra
class ChatCompletionStreamOutputTopLogprob(BaseInferenceType):
    logprob: float
    token: str


@dataclass_with_extra
class ChatCompletionStreamOutputLogprob(BaseInferenceType):
    logprob: float
    token: str
    top_logprobs: List[ChatCompletionStreamOutputTopLogprob]


@dataclass_with_extra
class ChatCompletionStreamOutputLogprobs(BaseInferenceType):
    content: List[ChatCompletionStreamOutputLogprob]


@dataclass_with_extra
class ChatCompletionStreamOutputChoice(BaseInferenceType):
    delta: ChatCompletionStreamOutputDelta
    index: int
    finish_reason: Optional[str] = None
    logprobs: Optional[ChatCompletionStreamOutputLogprobs] = None


@dataclass_with_extra
class ChatCompletionStreamOutputUsage(BaseInferenceType):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


@dataclass_with_extra
class ChatCompletionStreamOutput(BaseInferenceType):
    """Chat Completion Stream Output.
    Auto-generated from TGI specs.
    For more details, check out
    https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/scripts/inference-tgi-import.ts.
    """

    choices: List[ChatCompletionStreamOutputChoice]
    created: int
    id: str
    model: str
    system_fingerprint: str
    usage: Optional[ChatCompletionStreamOutputUsage] = None
