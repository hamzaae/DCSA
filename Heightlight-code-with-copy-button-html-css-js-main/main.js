document.addEventListener('DOMContentLoaded', () => {
    // hljs.initHighlightingOnLoad();
  
    const codeBlock = document.getElementById('code');
    const copyButton = document.getElementById('copy-button');
    const copySuccess = document.getElementById('copy-success');
  
    const copyTextHandler = () => {
      const text = codeBlock.innerText;
  
      // first version - document.execCommand('copy');
      // var element = document.createElement('textarea');
      // document.body.appendChild(element);
      // element.value = text;
      // element.select();
      // document.execCommand('copy');
      // document.body.removeChild(element);
  
      // copySuccess.classList.add('show-message');
      // setTimeout(() => {
      //   copySuccess.classList.remove('show-message');
      // }, 2500);
  
      //   second version - Clipboard API
      navigator.clipboard.writeText(text).then(
        () => {
          copyButton.innerHTML = "Copied!";
          setTimeout(() => {
            copyButton.innerHTML = "Copy";
          }, 1000);
          // copySuccess.classList.add('show-message');
          // setTimeout(() => {
          //   copySuccess.classList.remove('show-message');
          // }, 2500);
        },
        () => {
          console.log('Error writing to the clipboard');
        }
      );
    };
  
    copyButton.addEventListener('click', copyTextHandler);
  });