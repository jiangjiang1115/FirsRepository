console.log("打印预加载脚本");
var { contextBridge, ipcRenderer } = require('electron');

// require和contextBridge不可兼得

// contextBridge.exposeInMainWorld('versions', {
//   node: () => process.versions.node,
//   chrome: () => process.versions.chrome,
//   electron: () => process.versions.electron,
//   ping: () => ipcRenderer.invoke('ping')
//   // 除函数之外，我们也可以暴露变量
// })

