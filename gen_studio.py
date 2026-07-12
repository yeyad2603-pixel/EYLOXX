#!/usr/bin/env python3
"""Generator script for eylox-studio.html"""

import os

output_path = r"c:\Users\ip\Desktop\EYLOX\Eylox WEB html\eylox-studio.html"

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Eylox Studio</title>
<style>
:root{
  --purple:#a78bfa;--blue:#4fc3f7;--green:#4ade80;--red:#f87171;--yellow:#fbbf24;
  --bg:#06010f;--card:#0d0620;--card2:#120830;--border:#2a1a4a;
  --text:#e2d9f3;--muted:#7c6fa0;--hover:#1a0d35;
  --toolbar-h:42px;--menubar-h:32px;--bottom-h:130px;
  --left-w:240px;--right-w:260px;
}
*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',system-ui,sans-serif;}
body{background:var(--bg);color:var(--text);height:100vh;overflow:hidden;display:flex;flex-direction:column;}

/* ── LOADING ── */
#loading{position:fixed;inset:0;background:var(--bg);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;}
#loading h1{font-size:2.2rem;background:linear-gradient(135deg,var(--purple),var(--blue));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
#loading p{color:var(--muted);font-size:.9rem;}
.prog-bar{width:280px;height:6px;background:var(--card2);border-radius:3px;overflow:hidden;}
.prog-fill{height:100%;width:0%;background:linear-gradient(90deg,var(--purple),var(--blue));border-radius:3px;transition:width .3s ease;}

/* ── LOGIN ── */
#login-screen{position:fixed;inset:0;background:radial-gradient(ellipse at 50% 40%,#1a0545 0%,var(--bg) 70%);z-index:8888;display:none;align-items:center;justify-content:center;}
.login-box{background:rgba(13,6,32,.85);border:1px solid var(--border);border-radius:16px;padding:36px 40px;width:360px;backdrop-filter:blur(20px);box-shadow:0 0 60px rgba(167,139,250,.15);}
.login-box h2{font-size:1.5rem;margin-bottom:6px;background:linear-gradient(135deg,var(--purple),var(--blue));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.login-box p{color:var(--muted);font-size:.82rem;margin-bottom:24px;}
.login-box label{display:block;font-size:.78rem;color:var(--muted);margin-bottom:4px;margin-top:14px;}
.login-box input{width:100%;background:var(--card2);border:1px solid var(--border);border-radius:8px;padding:9px 12px;color:var(--text);font-size:.9rem;outline:none;transition:border-color .2s;}
.login-box input:focus{border-color:var(--purple);}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:9px 18px;border:none;border-radius:8px;cursor:pointer;font-size:.85rem;font-weight:600;transition:all .2s;}
.btn-primary{background:linear-gradient(135deg,var(--purple),#7c3aed);color:#fff;}
.btn-primary:hover{opacity:.9;transform:translateY(-1px);box-shadow:0 4px 20px rgba(167,139,250,.35);}
.btn-ghost{background:transparent;color:var(--muted);border:1px solid var(--border);}
.btn-ghost:hover{border-color:var(--purple);color:var(--purple);}
.login-actions{display:flex;gap:10px;margin-top:20px;}
.login-error{color:var(--red);font-size:.8rem;margin-top:8px;min-height:18px;}

/* ── STUDIO LAYOUT ── */
#studio{display:none;flex-direction:column;height:100vh;}
#studio.visible{display:flex;}

/* menubar */
#menubar{height:var(--menubar-h);background:rgba(13,6,32,.95);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 8px;gap:2px;backdrop-filter:blur(10px);flex-shrink:0;z-index:100;}
.menu-logo{font-size:.85rem;font-weight:700;background:linear-gradient(135deg,var(--purple),var(--blue));-webkit-background-clip:text;-webkit-text-fill-color:transparent;padding:0 10px;margin-right:4px;white-space:nowrap;}
.menu-item{position:relative;}
.menu-btn{background:none;border:none;color:var(--text);font-size:.78rem;padding:4px 10px;border-radius:5px;cursor:pointer;white-space:nowrap;}
.menu-btn:hover{background:var(--hover);color:var(--purple);}
.dropdown{position:absolute;top:100%;left:0;background:rgba(18,8,48,.97);border:1px solid var(--border);border-radius:8px;min-width:190px;padding:4px;z-index:500;display:none;box-shadow:0 8px 32px rgba(0,0,0,.5);backdrop-filter:blur(16px);}
.dropdown.open{display:block;}
.dd-item{display:block;width:100%;background:none;border:none;color:var(--text);font-size:.78rem;padding:6px 12px;border-radius:5px;cursor:pointer;text-align:left;display:flex;justify-content:space-between;align-items:center;}
.dd-item:hover{background:var(--hover);color:var(--purple);}
.dd-sep{height:1px;background:var(--border);margin:3px 6px;}
.dd-kbd{color:var(--muted);font-size:.7rem;}
.menu-spacer{flex:1;}
.menu-user{font-size:.75rem;color:var(--muted);padding:0 10px;}
.menu-back{font-size:.75rem;color:var(--muted);padding:4px 10px;border-radius:5px;cursor:pointer;text-decoration:none;border:1px solid var(--border);}
.menu-back:hover{border-color:var(--purple);color:var(--purple);}

/* toolbar */
#toolbar{height:var(--toolbar-h);background:rgba(13,6,32,.9);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 10px;gap:6px;flex-shrink:0;}
.tb-group{display:flex;align-items:center;gap:3px;padding:0 6px;border-right:1px solid var(--border);}
.tb-group:last-child{border-right:none;}
.tb-btn{background:none;border:1px solid transparent;color:var(--muted);font-size:.78rem;padding:5px 10px;border-radius:6px;cursor:pointer;display:flex;align-items:center;gap:5px;white-space:nowrap;transition:all .15s;}
.tb-btn:hover{border-color:var(--border);color:var(--text);background:var(--hover);}
.tb-btn.active{background:rgba(167,139,250,.15);border-color:var(--purple);color:var(--purple);}
.tb-sep{width:1px;height:22px;background:var(--border);}
.tb-label{font-size:.7rem;color:var(--muted);}
#play-btn{background:linear-gradient(135deg,var(--green),#16a34a);color:#000;border:none;font-weight:700;padding:5px 16px;}
#play-btn:hover{opacity:.9;}
#stop-btn{background:linear-gradient(135deg,var(--red),#dc2626);color:#fff;border:none;font-weight:700;padding:5px 16px;display:none;}

/* main area */
#main{flex:1;display:flex;overflow:hidden;}

/* left panel */
#left-panel{width:var(--left-w);background:rgba(13,6,32,.85);border-right:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;backdrop-filter:blur(8px);}
.panel-tabs{display:flex;border-bottom:1px solid var(--border);}
.panel-tab{flex:1;background:none;border:none;color:var(--muted);font-size:.75rem;padding:8px;cursor:pointer;border-bottom:2px solid transparent;transition:all .15s;}
.panel-tab.active{color:var(--purple);border-bottom-color:var(--purple);}
.panel-tab:hover:not(.active){color:var(--text);}
.panel-content{flex:1;overflow-y:auto;padding:6px;}
.panel-content::-webkit-scrollbar{width:4px;}
.panel-content::-webkit-scrollbar-track{background:transparent;}
.panel-content::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px;}
.panel-section{margin-bottom:4px;}
.panel-section-header{font-size:.7rem;color:var(--muted);padding:4px 6px;text-transform:uppercase;letter-spacing:.05em;}

/* explorer tree */
.tree-item{display:flex;align-items:center;gap:5px;padding:3px 6px;border-radius:5px;cursor:pointer;font-size:.78rem;user-select:none;}
.tree-item:hover{background:var(--hover);}
.tree-item.selected{background:rgba(167,139,250,.15);color:var(--purple);}
.tree-icon{font-size:.85rem;flex-shrink:0;}
.tree-arrow{font-size:.6rem;color:var(--muted);flex-shrink:0;width:12px;}
.tree-children{padding-left:14px;}

/* toolbox */
.toolbox-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;padding:4px;}
.tool-card{background:var(--card2);border:1px solid var(--border);border-radius:8px;padding:10px 4px;display:flex;flex-direction:column;align-items:center;gap:5px;cursor:pointer;transition:all .15s;font-size:.68rem;color:var(--muted);text-align:center;}
.tool-card:hover{border-color:var(--purple);color:var(--purple);background:rgba(167,139,250,.08);transform:translateY(-1px);}
.tool-icon{font-size:1.4rem;}

/* viewport */
#viewport-wrap{flex:1;display:flex;flex-direction:column;position:relative;}
#viewport{flex:1;position:relative;overflow:hidden;background:#000;}
#viewport canvas{display:block;width:100%!important;height:100%!important;}
.viewport-overlay{position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:10;}
.vp-info{position:absolute;bottom:8px;left:8px;font-size:.7rem;color:rgba(255,255,255,.4);z-index:10;pointer-events:none;}
.vp-mode-badge{position:absolute;top:8px;left:50%;transform:translateX(-50%);background:rgba(74,222,128,.2);border:1px solid var(--green);color:var(--green);font-size:.75rem;padding:3px 14px;border-radius:20px;z-index:10;display:none;}

/* right panel */
#right-panel{width:var(--right-w);background:rgba(13,6,32,.85);border-left:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;backdrop-filter:blur(8px);}
#right-panel .panel-tabs{border-bottom:1px solid var(--border);}
.props-section{margin-bottom:10px;}
.props-title{font-size:.68rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;padding:6px 8px 3px;border-bottom:1px solid var(--border);margin-bottom:6px;}
.prop-row{display:flex;align-items:center;padding:3px 8px;gap:6px;}
.prop-label{font-size:.73rem;color:var(--muted);flex:0 0 60px;}
.prop-val{flex:1;display:flex;gap:3px;}
.prop-input{background:var(--card2);border:1px solid var(--border);border-radius:5px;color:var(--text);font-size:.75rem;padding:3px 6px;width:100%;outline:none;}
.prop-input:focus{border-color:var(--purple);}
.prop-input[type=number]{-moz-appearance:textfield;}
.prop-input[type=number]::-webkit-outer-spin-button,
.prop-input[type=number]::-webkit-inner-spin-button{-webkit-appearance:none;}
.prop-color{width:36px;height:24px;border:1px solid var(--border);border-radius:5px;padding:1px;background:var(--card2);cursor:pointer;}
.prop-toggle{position:relative;display:inline-block;width:32px;height:17px;}
.prop-toggle input{opacity:0;width:0;height:0;}
.toggle-slider{position:absolute;inset:0;background:var(--card2);border:1px solid var(--border);border-radius:17px;cursor:pointer;transition:.2s;}
.toggle-slider:before{content:'';position:absolute;width:11px;height:11px;left:2px;top:2px;background:var(--muted);border-radius:50%;transition:.2s;}
.prop-toggle input:checked+.toggle-slider{background:rgba(167,139,250,.3);border-color:var(--purple);}
.prop-toggle input:checked+.toggle-slider:before{transform:translateX(15px);background:var(--purple);}
.slider-wrap{flex:1;display:flex;align-items:center;gap:6px;}
.prop-slider{-webkit-appearance:none;width:100%;height:4px;border-radius:2px;background:var(--card2);outline:none;cursor:pointer;}
.prop-slider::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:var(--purple);cursor:pointer;}
.prop-select{background:var(--card2);border:1px solid var(--border);border-radius:5px;color:var(--text);font-size:.75rem;padding:3px 6px;width:100%;outline:none;}
.no-select{color:var(--muted);font-size:.78rem;text-align:center;padding:30px 10px;}

/* script editor */
#script-editor{display:none;flex-direction:column;height:100%;}
.script-header{display:flex;align-items:center;gap:8px;padding:6px 10px;border-bottom:1px solid var(--border);background:var(--card2);}
.script-name{font-size:.8rem;color:var(--purple);}
.script-close{background:none;border:none;color:var(--muted);cursor:pointer;font-size:1rem;margin-left:auto;}
.script-close:hover{color:var(--red);}
#script-area{flex:1;display:flex;overflow:hidden;}
#line-numbers{background:var(--card2);color:var(--muted);font-family:monospace;font-size:.8rem;padding:8px 6px;text-align:right;user-select:none;min-width:36px;border-right:1px solid var(--border);overflow:hidden;}
#code-input{flex:1;background:#0a0520;color:#c9d1d9;font-family:'Cascadia Code','Fira Code',monospace;font-size:.8rem;padding:8px;border:none;outline:none;resize:none;line-height:1.5;tab-size:2;}

/* bottom console */
#bottom{height:var(--bottom-h);background:rgba(13,6,32,.9);border-top:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;}
.bottom-tabs{display:flex;border-bottom:1px solid var(--border);}
.bottom-tab{background:none;border:none;color:var(--muted);font-size:.73rem;padding:5px 14px;cursor:pointer;border-bottom:2px solid transparent;}
.bottom-tab.active{color:var(--blue);border-bottom-color:var(--blue);}
#console-output{flex:1;overflow-y:auto;padding:4px 8px;font-family:monospace;font-size:.75rem;}
.con-line{padding:1px 0;border-bottom:1px solid rgba(255,255,255,.03);}
.con-info{color:var(--blue);}
.con-warn{color:var(--yellow);}
.con-err{color:var(--red);}
.con-ok{color:var(--green);}

/* context menu */
#ctx-menu{position:fixed;background:rgba(18,8,48,.97);border:1px solid var(--border);border-radius:8px;min-width:170px;padding:4px;z-index:600;display:none;box-shadow:0 8px 32px rgba(0,0,0,.5);backdrop-filter:blur(16px);}
.ctx-item{display:block;width:100%;background:none;border:none;color:var(--text);font-size:.78rem;padding:6px 12px;border-radius:5px;cursor:pointer;text-align:left;}
.ctx-item:hover{background:var(--hover);color:var(--purple);}
.ctx-sep{height:1px;background:var(--border);margin:3px 6px;}

/* resize handle */
.resize-h{cursor:row-resize;height:4px;background:var(--border);transition:background .15s;}
.resize-h:hover{background:var(--purple);}

/* scrollbars global */
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}

/* util */
.hidden{display:none!important;}
.flex-center{display:flex;align-items:center;justify-content:center;}
</style>
</head>
<body>

<!-- LOADING -->
<div id="loading">
  <h1>&#x2B22; EYLOX STUDIO</h1>
  <p>Initializing workspace...</p>
  <div class="prog-bar"><div class="prog-fill" id="prog-fill"></div></div>
  <p id="prog-label" style="font-size:.75rem;color:var(--muted)">Loading engine...</p>
</div>

<!-- LOGIN -->
<div id="login-screen">
  <div class="login-box">
    <h2>&#x2B22; Eylox Studio</h2>
    <p>Sign in to start building</p>
    <label>Username</label>
    <input type="text" id="li-user" placeholder="Username" autocomplete="username"/>
    <label>Password</label>
    <input type="password" id="li-pass" placeholder="Password" autocomplete="current-password"/>
    <div class="login-error" id="li-err"></div>
    <div class="login-actions">
      <button class="btn btn-primary" onclick="doLogin()">Sign In</button>
      <button class="btn btn-ghost" onclick="doGuest()">Continue as Guest</button>
    </div>
  </div>
</div>

<!-- STUDIO -->
<div id="studio">

  <!-- MENUBAR -->
  <div id="menubar">
    <span class="menu-logo">&#x2B22; EYLOX</span>
    <!-- File -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-file')">File</button>
      <div class="dropdown" id="m-file">
        <button class="dd-item" onclick="newScene();closeMenus()">New Scene <span class="dd-kbd">Ctrl+N</span></button>
        <button class="dd-item" onclick="saveScene();closeMenus()">Save <span class="dd-kbd">Ctrl+S</span></button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="exportHTML();closeMenus()">Export as HTML</button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="closeMenus();window.location.href='index.html'">Back to Home</button>
      </div>
    </div>
    <!-- Edit -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-edit')">Edit</button>
      <div class="dropdown" id="m-edit">
        <button class="dd-item" onclick="undo();closeMenus()">Undo <span class="dd-kbd">Ctrl+Z</span></button>
        <button class="dd-item" onclick="redo();closeMenus()">Redo <span class="dd-kbd">Ctrl+Y</span></button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="cutObj();closeMenus()">Cut <span class="dd-kbd">Ctrl+X</span></button>
        <button class="dd-item" onclick="copyObj();closeMenus()">Copy <span class="dd-kbd">Ctrl+C</span></button>
        <button class="dd-item" onclick="pasteObj();closeMenus()">Paste <span class="dd-kbd">Ctrl+V</span></button>
        <button class="dd-item" onclick="duplicateObj();closeMenus()">Duplicate <span class="dd-kbd">Ctrl+D</span></button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="deleteSelected();closeMenus()">Delete <span class="dd-kbd">Del</span></button>
      </div>
    </div>
    <!-- View -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-view')">View</button>
      <div class="dropdown" id="m-view">
        <button class="dd-item" onclick="togglePanel('left-panel');closeMenus()">Explorer Panel</button>
        <button class="dd-item" onclick="togglePanel('right-panel');closeMenus()">Properties Panel</button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="toggleGrid();closeMenus()">Toggle Grid <span class="dd-kbd">G</span></button>
        <button class="dd-item" onclick="toggleWireframe();closeMenus()">Toggle Wireframe</button>
        <button class="dd-item" onclick="resetCamera();closeMenus()">Reset Camera</button>
      </div>
    </div>
    <!-- Insert -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-insert')">Insert</button>
      <div class="dropdown" id="m-insert">
        <button class="dd-item" onclick="insertObject('Part');closeMenus()">Part (Box)</button>
        <button class="dd-item" onclick="insertObject('Sphere');closeMenus()">Sphere</button>
        <button class="dd-item" onclick="insertObject('Cylinder');closeMenus()">Cylinder</button>
        <button class="dd-item" onclick="insertObject('Wedge');closeMenus()">Wedge (Cone)</button>
        <button class="dd-item" onclick="insertObject('Torus');closeMenus()">Torus</button>
        <button class="dd-item" onclick="insertObject('Cone');closeMenus()">Cone</button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="insertObject('Spawn');closeMenus()">Spawn Point</button>
        <button class="dd-item" onclick="insertObject('PointLight');closeMenus()">Point Light</button>
        <button class="dd-item" onclick="insertObject('SpotLight');closeMenus()">Spot Light</button>
        <div class="dd-sep"></div>
        <button class="dd-item" onclick="insertObject('Script');closeMenus()">Script</button>
        <button class="dd-item" onclick="insertObject('Model');closeMenus()">Model Group</button>
      </div>
    </div>
    <!-- Terrain -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-terrain')">Terrain</button>
      <div class="dropdown" id="m-terrain">
        <button class="dd-item" onclick="conLog('Terrain editor coming soon','warn');closeMenus()">Paint Terrain</button>
        <button class="dd-item" onclick="conLog('Terrain editor coming soon','warn');closeMenus()">Smooth Terrain</button>
        <button class="dd-item" onclick="conLog('Terrain editor coming soon','warn');closeMenus()">Generate Terrain</button>
      </div>
    </div>
    <!-- Test -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-test')">Test</button>
      <div class="dropdown" id="m-test">
        <button class="dd-item" onclick="startPlay();closeMenus()">Play <span class="dd-kbd">F5</span></button>
        <button class="dd-item" onclick="stopPlay();closeMenus()">Stop <span class="dd-kbd">F6</span></button>
      </div>
    </div>
    <!-- Publish -->
    <div class="menu-item">
      <button class="menu-btn" onclick="publishGame();closeMenus()">Publish</button>
    </div>
    <!-- Settings -->
    <div class="menu-item">
      <button class="menu-btn" onclick="toggleMenu('m-settings')">Settings</button>
      <div class="dropdown" id="m-settings">
        <button class="dd-item" onclick="conLog('Settings panel coming soon','info');closeMenus()">Studio Settings</button>
        <button class="dd-item" onclick="conLog('Theme options coming soon','info');closeMenus()">Theme</button>
      </div>
    </div>
    <div class="menu-spacer"></div>
    <span class="menu-user" id="menu-user-label">Guest</span>
    <a class="menu-back" href="index.html">&#8592; Home</a>
  </div>

  <!-- TOOLBAR -->
  <div id="toolbar">
    <div class="tb-group">
      <button class="tb-btn active" id="tb-select" onclick="setTool('select')" title="Select (Q)">&#9654; Select</button>
      <button class="tb-btn" id="tb-move" onclick="setTool('move')" title="Move (W)">&#10021; Move</button>
      <button class="tb-btn" id="tb-scale" onclick="setTool('scale')" title="Scale (E)">&#11020; Scale</button>
      <button class="tb-btn" id="tb-rotate" onclick="setTool('rotate')" title="Rotate (R)">&#8635; Rotate</button>
    </div>
    <div class="tb-group">
      <button class="tb-btn" onclick="insertObject('Part')" title="Insert Part">&#9646; Part</button>
      <button class="tb-btn" onclick="insertObject('Sphere')">&#9711; Sphere</button>
      <button class="tb-btn" onclick="insertObject('PointLight')">&#9728; Light</button>
    </div>
    <div class="tb-group">
      <span class="tb-label">Snap:</span>
      <select id="snap-val" class="prop-select" style="width:70px;font-size:.72rem;" onchange="updateSnap()">
        <option value="0">Off</option>
        <option value="0.5">0.5</option>
        <option value="1" selected>1</option>
        <option value="2">2</option>
        <option value="4">4</option>
      </select>
    </div>
    <div class="tb-group" style="margin-left:auto;">
      <button class="tb-btn" id="play-btn" onclick="startPlay()" title="Play (F5)">&#9654; Play</button>
      <button class="tb-btn" id="stop-btn" onclick="stopPlay()" title="Stop (F6)">&#9646;&#9646; Stop</button>
    </div>
  </div>

  <!-- MAIN -->
  <div id="main">

    <!-- LEFT PANEL -->
    <div id="left-panel">
      <div class="panel-tabs">
        <button class="panel-tab active" onclick="switchLeftTab('explorer',this)">Explorer</button>
        <button class="panel-tab" onclick="switchLeftTab('toolbox',this)">Toolbox</button>
      </div>
      <!-- Explorer -->
      <div class="panel-content" id="tab-explorer">
        <div id="scene-tree"></div>
      </div>
      <!-- Toolbox -->
      <div class="panel-content hidden" id="tab-toolbox">
        <div class="toolbox-grid" id="toolbox-grid"></div>
      </div>
    </div>

    <!-- VIEWPORT WRAP -->
    <div id="viewport-wrap">
      <div id="viewport">
        <div class="viewport-overlay">
          <button class="tb-btn" style="font-size:.7rem;padding:3px 8px;" onclick="resetCamera()">&#8635; Reset</button>
        </div>
        <div class="vp-info" id="vp-info">Eylox Studio | Ctrl+Z Undo | Q/W/E/R Tools | F5 Play</div>
        <div class="vp-mode-badge" id="vp-badge">&#9654; PLAY MODE</div>
      </div>
      <div id="bottom">
        <div class="bottom-tabs">
          <button class="bottom-tab active" onclick="switchBottomTab('console',this)">Output</button>
          <button class="bottom-tab" onclick="switchBottomTab('errors',this)">Errors</button>
        </div>
        <div id="console-output"></div>
      </div>
    </div>

    <!-- RIGHT PANEL -->
    <div id="right-panel">
      <div class="panel-tabs">
        <button class="panel-tab active" onclick="switchRightTab('props',this)">Properties</button>
        <button class="panel-tab" onclick="switchRightTab('script',this)">Script</button>
      </div>
      <!-- Properties -->
      <div class="panel-content" id="tab-props" style="padding:0;">
        <div id="props-body"><div class="no-select">Select an object to edit its properties.</div></div>
      </div>
      <!-- Script editor -->
      <div id="script-editor" style="flex:1;">
        <div class="script-header">
          <span class="tree-icon">&#128196;</span>
          <span class="script-name" id="script-editor-name">Script</span>
          <button class="script-close" onclick="closeScriptEditor()">&#x2715;</button>
        </div>
        <div id="script-area">
          <div id="line-numbers">1</div>
          <textarea id="code-input" spellcheck="false" placeholder="-- Eylox Script&#10;-- Write your game logic here"></textarea>
        </div>
      </div>
    </div>

  </div><!-- /main -->
</div><!-- /studio -->

<!-- CONTEXT MENU -->
<div id="ctx-menu">
  <button class="ctx-item" onclick="insertObject('Part');closeCtx()">&#9646; Insert Part</button>
  <button class="ctx-item" onclick="insertObject('Sphere');closeCtx()">&#9711; Insert Sphere</button>
  <button class="ctx-item" onclick="insertObject('PointLight');closeCtx()">&#9728; Insert Light</button>
  <div class="ctx-sep"></div>
  <button class="ctx-item" onclick="duplicateObj();closeCtx()">&#10064; Duplicate</button>
  <button class="ctx-item" onclick="focusSelected();closeCtx()">&#9654; Focus (F)</button>
  <div class="ctx-sep"></div>
  <button class="ctx-item" onclick="deleteSelected();closeCtx()" style="color:var(--red)">&#128465; Delete</button>
</div>

<!-- THREE.JS -->
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/TransformControls.js"></script>

<script>
'use strict';
// ═══════════════════════════════════════
//  EYLOX STUDIO — Main Script
// ═══════════════════════════════════════

// ── Auth ──────────────────────────────
function checkAuth(){
  const t=localStorage.getItem('eylox_token');
  const g=localStorage.getItem('eylox_guest');
  const u=localStorage.getItem('eylox_user');
  if(t||g||u) return true;
  return false;
}
function doLogin(){
  const u=document.getElementById('li-user').value.trim();
  const p=document.getElementById('li-pass').value;
  const err=document.getElementById('li-err');
  if(u==='Eylox'&&p==='EyadYasser'){
    localStorage.setItem('eylox_user','Eylox');
    localStorage.setItem('eylox_token','owner-token-eylox');
    initStudio();
  } else if(u&&p){
    // normal user
    localStorage.setItem('eylox_user',u);
    localStorage.setItem('eylox_token','user-token-'+Date.now());
    initStudio();
  } else {
    err.textContent='Invalid credentials.';
  }
}
function doGuest(){
  localStorage.setItem('eylox_guest','1');
  initStudio();
}
document.getElementById('li-pass').addEventListener('keydown',e=>{if(e.key==='Enter')doLogin();});

// ── Loading & Init ────────────────────
const progFill=document.getElementById('prog-fill');
const progLabel=document.getElementById('prog-label');
function setProgress(pct,msg){
  progFill.style.width=pct+'%';
  if(msg)progLabel.textContent=msg;
}

function beginLoading(){
  setProgress(5,'Checking session...');
  setTimeout(()=>setProgress(20,'Loading Three.js engine...'),100);
  setTimeout(()=>setProgress(45,'Building 3D scene...'),400);
  setTimeout(()=>setProgress(70,'Initializing UI...'),700);
  setTimeout(()=>setProgress(90,'Ready...'),1000);
  setTimeout(()=>{
    setProgress(100,'');
    if(!checkAuth()){
      document.getElementById('loading').style.display='none';
      const ls=document.getElementById('login-screen');
      ls.style.display='flex';
    } else {
      initStudio();
    }
  },1300);
}

function initStudio(){
  document.getElementById('loading').style.display='none';
  document.getElementById('login-screen').style.display='none';
  const studio=document.getElementById('studio');
  studio.classList.add('visible');
  const u=localStorage.getItem('eylox_user')||'Guest';
  document.getElementById('menu-user-label').textContent=u;
  initThree();
  buildToolbox();
  buildExplorer();
  conLog('Eylox Studio loaded. Welcome, '+u+'!','ok');
  conLog('Press F5 to test your game. Ctrl+S to save.','info');
}

beginLoading();

// ── Three.js Core ─────────────────────
let scene,camera,renderer,orbitControls,transformControls;
let raycaster,mouse;
let gridHelper,axesHelper,fogEnabled=true;
let wireframeMode=false;
let snapValue=1;

// Scene objects registry
let sceneObjects=[]; // {id,name,type,mesh,children,script,props}
let selected=null;
let clipboard=null;

// Undo/Redo
const undoStack=[];
const redoStack=[];
const MAX_UNDO=50;

// Play mode
let playMode=false;
let playerObj=null;
let playerVel=new THREE.Vector3();
let playerOnGround=false;
let keysHeld={};
let playerPitch=0,playerYaw=0;
let editCamPos=new THREE.Vector3();
let editCamTarget=new THREE.Vector3();
let pointerLocked=false;

function initThree(){
  const vp=document.getElementById('viewport');
  // Renderer
  renderer=new THREE.WebGLRenderer({antialias:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  renderer.shadowMap.enabled=true;
  renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure=0.9;
  renderer.outputEncoding=THREE.sRGBEncoding;
  vp.appendChild(renderer.domElement);
  resizeRenderer();

  // Scene
  scene=new THREE.Scene();
  scene.background=new THREE.Color(0x0a0318);
  scene.fog=new THREE.Fog(0x0a0318,50,200);

  // Camera
  camera=new THREE.PerspectiveCamera(60,1,0.1,2000);
  camera.position.set(18,14,22);
  camera.lookAt(0,0,0);

  // Sky sphere
  const skyGeo=new THREE.SphereGeometry(400,32,32);
  const skyMat=new THREE.MeshBasicMaterial({
    color:0x0a0318,side:THREE.BackSide
  });
  const sky=new THREE.Mesh(skyGeo,skyMat);
  scene.add(sky);

  // Lighting
  const ambient=new THREE.AmbientLight(0x8060d0,0.4);
  scene.add(ambient);
  const dirLight=new THREE.DirectionalLight(0xffffff,1.1);
  dirLight.position.set(20,30,20);
  dirLight.castShadow=true;
  dirLight.shadow.mapSize.set(2048,2048);
  dirLight.shadow.camera.near=0.5;
  dirLight.shadow.camera.far=200;
  dirLight.shadow.camera.left=-40;
  dirLight.shadow.camera.right=40;
  dirLight.shadow.camera.top=40;
  dirLight.shadow.camera.bottom=-40;
  scene.add(dirLight);
  const hemi=new THREE.HemisphereLight(0x4fc3f7,0x2d1b69,0.35);
  scene.add(hemi);

  // Baseplate
  const bpGeo=new THREE.BoxGeometry(100,1,100);
  const bpMat=new THREE.MeshStandardMaterial({
    color:0x2a1a5a,roughness:.85,metalness:.1,
  });
  const bp=new THREE.Mesh(bpGeo,bpMat);
  bp.position.y=-0.5;
  bp.receiveShadow=true;
  scene.add(bp);
  const bpEntry={id:genId(),name:'Baseplate',type:'Baseplate',mesh:bp,isBasePlate:true,props:{color:'#2a1a5a',roughness:.85,metalness:.1,anchored:true,canCollide:true,visible:true}};
  sceneObjects.push(bpEntry);
  bp.userData.studioId=bpEntry.id;

  // Grid
  gridHelper=new THREE.GridHelper(100,50,0x3b1e7a,0x1e0e3a);
  scene.add(gridHelper);

  // Axes
  axesHelper=new THREE.AxesHelper(5);
  axesHelper.position.y=0.01;
  scene.add(axesHelper);

  // OrbitControls
  orbitControls=new THREE.OrbitControls(camera,renderer.domElement);
  orbitControls.enableDamping=true;
  orbitControls.dampingFactor=0.08;
  orbitControls.minDistance=2;
  orbitControls.maxDistance=500;
  orbitControls.maxPolarAngle=Math.PI*0.9;

  // TransformControls
  transformControls=new THREE.TransformControls(camera,renderer.domElement);
  transformControls.setSpace('world');
  transformControls.setTranslationSnap(snapValue||null);
  transformControls.setRotationSnap(THREE.MathUtils.degToRad(15));
  transformControls.setScaleSnap(0.25);
  scene.add(transformControls);
  transformControls.addEventListener('dragging-changed',e=>{
    orbitControls.enabled=!e.value;
  });
  transformControls.addEventListener('objectChange',()=>{
    if(selected) updatePropsFromMesh();
  });
  transformControls.addEventListener('mouseUp',()=>{
    pushUndo();
  });

  // Raycaster
  raycaster=new THREE.Raycaster();
  mouse=new THREE.Vector2();

  // Events
  renderer.domElement.addEventListener('click',onViewportClick);
  renderer.domElement.addEventListener('contextmenu',onViewportRightClick);
  window.addEventListener('keydown',onKeyDown);
  window.addEventListener('keyup',e=>{keysHeld[e.code]=false;});
  window.addEventListener('resize',resizeRenderer);
  document.addEventListener('click',e=>{
    if(!e.target.closest('.menu-item')) closeMenus();
    if(!e.target.closest('#ctx-menu')) closeCtx();
  });
  document.addEventListener('mousemove',onMouseMove);
  document.addEventListener('pointerlockchange',()=>{
    pointerLocked=document.pointerLockElement===renderer.domElement;
  });

  // Render loop
  animate();
  resizeRenderer();
}

function resizeRenderer(){
  const vp=document.getElementById('viewport');
  const w=vp.clientWidth,h=vp.clientHeight;
  if(w===0||h===0)return;
  renderer.setSize(w,h,false);
  camera.aspect=w/h;
  camera.updateProjectionMatrix();
}

let clock=new THREE.Clock();
function animate(){
  requestAnimationFrame(animate);
  const dt=clock.getDelta();
  if(playMode) updatePlayer(dt);
  else orbitControls.update();
  renderer.render(scene,camera);
}

// ── Tool Management ───────────────────
let currentTool='select';
function setTool(t){
  currentTool=t;
  ['select','move','scale','rotate'].forEach(n=>{
    document.getElementById('tb-'+n).classList.toggle('active',n===t);
  });
  if(!selected){return;}
  if(t==='move'){transformControls.setMode('translate');transformControls.attach(selected.mesh);}
  else if(t==='scale'){transformControls.setMode('scale');transformControls.attach(selected.mesh);}
  else if(t==='rotate'){transformControls.setMode('rotate');transformControls.attach(selected.mesh);}
  else{transformControls.detach();}
}
function updateSnap(){
  snapValue=parseFloat(document.getElementById('snap-val').value)||0;
  if(transformControls){
    transformControls.setTranslationSnap(snapValue>0?snapValue:null);
  }
}

// ── Object IDs ────────────────────────
let _idCtr=100;
function genId(){return 'obj_'+(++_idCtr);}
let _nameCounters={};
function uniqueName(base){
  _nameCounters[base]=(_nameCounters[base]||0)+1;
  return _nameCounters[base]===1?base:base+_nameCounters[base];
}

// ── Insert Objects ────────────────────
const TYPE_ICONS={
  Part:'&#9646;',Sphere:'&#9711;',Cylinder:'&#11618;',Wedge:'&#11176;',
  Torus:'&#9737;',Cone:'&#9651;',Spawn:'&#9654;',PointLight:'&#9728;',
  SpotLight:'&#9681;',Script:'&#128196;',Model:'&#128194;',Baseplate:'&#9644;'
};

function insertObject(type,pos){
  pos=pos||new THREE.Vector3(0,1,0);
  let mesh,geo,mat;
  const color=randomColor();
  mat=new THREE.MeshStandardMaterial({color:new THREE.Color(color),roughness:.7,metalness:.05,shadowSide:THREE.FrontSide});

  switch(type){
    case'Part':
      geo=new THREE.BoxGeometry(2,2,2);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Sphere':
      geo=new THREE.SphereGeometry(1,32,32);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Cylinder':
      geo=new THREE.CylinderGeometry(1,1,2,32);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Wedge':
      geo=new THREE.ConeGeometry(1,2,4);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Torus':
      geo=new THREE.TorusGeometry(1,.4,16,48);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Cone':
      geo=new THREE.ConeGeometry(1,2,32);
      mesh=new THREE.Mesh(geo,mat);
      break;
    case'Spawn':{
      geo=new THREE.CylinderGeometry(1,.8,.1,32);
      const sm=new THREE.MeshStandardMaterial({color:0x4ade80,roughness:.5,metalness:.2,emissive:0x1a5c30});
      mesh=new THREE.Mesh(geo,sm);
      break;}
    case'PointLight':{
      geo=new THREE.SphereGeometry(.25,16,16);
      const lm=new THREE.MeshBasicMaterial({color:0xfbbf24});
      mesh=new THREE.Mesh(geo,lm);
      const pl=new THREE.PointLight(0xffd966,2,20);
      mesh.add(pl);
      break;}
    case'SpotLight':{
      geo=new THREE.ConeGeometry(.3,.6,16);
      const slm=new THREE.MeshBasicMaterial({color:0x4fc3f7});
      mesh=new THREE.Mesh(geo,slm);
      const sl=new THREE.SpotLight(0x4fc3f7,3,30,Math.PI/6,.3);
      sl.position.set(0,0,0);
      sl.target.position.set(0,-1,0);
      mesh.add(sl);
      mesh.add(sl.target);
      break;}
    case'Script':{
      // Virtual object — no mesh, represented as group
      const sg=new THREE.Group();
      scene.add(sg);
      sg.position.copy(pos);
      const id=genId();
      const name=uniqueName('Script');
      const entry={id,name,type:'Script',mesh:sg,isVirtual:true,script:'-- Script: '+name+'\n\nfunction onStart()\n  print("Hello from "+name+"!")\nend\n',props:{visible:true}};
      sceneObjects.push(entry);
      sg.userData.studioId=id;
      selectObject(entry);
      buildExplorer();
      conLog('Inserted Script: '+name,'info');
      return;
    }
    case'Model':{
      const mg=new THREE.Group();
      scene.add(mg);
      mg.position.copy(pos);
      const id=genId();
      const name=uniqueName('Model');
      const entry={id,name,type:'Model',mesh:mg,isGroup:true,children:[],props:{visible:true}};
      sceneObjects.push(entry);
      mg.userData.studioId=id;
      selectObject(entry);
      buildExplorer();
      conLog('Inserted Model group: '+name,'info');
      return;
    }
    default:
      geo=new THREE.BoxGeometry(2,2,2);
      mesh=new THREE.Mesh(geo,mat);
  }

  mesh.castShadow=true;
  mesh.receiveShadow=true;
  mesh.position.copy(pos);
  scene.add(mesh);

  const id=genId();
  const name=uniqueName(type);
  const props={color,roughness:.7,metalness:.05,anchored:false,canCollide:true,visible:true};
  const entry={id,name,type,mesh,props};
  mesh.userData.studioId=id;
  sceneObjects.push(entry);
  pushUndo();
  selectObject(entry);
  buildExplorer();
  conLog('Inserted '+type+': '+name,'info');
}

function randomColor(){
  const palette=['#a78bfa','#4fc3f7','#4ade80','#f87171','#fbbf24','#e879f9','#38bdf8','#fb923c'];
  return palette[Math.floor(Math.random()*palette.length)];
}

// ── Selection ─────────────────────────
function selectObject(entry){
  // deselect old
  if(selected&&selected.mesh.material&&!selected.isVirtual){
    if(Array.isArray(selected.mesh.material)){
      selected.mesh.material.forEach(m=>m.emissive&&m.emissive.set(0,0,0));
    } else if(selected.mesh.material.emissive){
      selected.mesh.material.emissive.set(0,0,0);
    }
  }
  selected=entry;
  if(entry&&entry.mesh){
    if(!entry.isVirtual&&!entry.isGroup){
      if(entry.mesh.material&&entry.mesh.material.emissive)
        entry.mesh.material.emissive.set(0.08,0.04,0.2);
      if(currentTool==='move'){transformControls.setMode('translate');transformControls.attach(entry.mesh);}
      else if(currentTool==='scale'){transformControls.setMode('scale');transformControls.attach(entry.mesh);}
      else if(currentTool==='rotate'){transformControls.setMode('rotate');transformControls.attach(entry.mesh);}
      else{transformControls.detach();}
    } else {
      transformControls.detach();
    }
  } else {
    transformControls.detach();
  }
  buildPropsPanel();
  buildExplorer();
}

function deselectAll(){
  selectObject(null);
}

function onViewportClick(e){
  if(playMode)return;
  if(transformControls.dragging)return;
  const rect=renderer.domElement.getBoundingClientRect();
  mouse.x=((e.clientX-rect.left)/rect.width)*2-1;
  mouse.y=-((e.clientY-rect.top)/rect.height)*2+1;
  raycaster.setFromCamera(mouse,camera);
  const meshes=sceneObjects.filter(o=>o.mesh&&o.mesh.isMesh).map(o=>o.mesh);
  const hits=raycaster.intersectObjects(meshes,false);
  if(hits.length>0){
    const sid=hits[0].object.userData.studioId;
    const entry=sceneObjects.find(o=>o.id===sid);
    if(entry) selectObject(entry);
  } else {
    deselectAll();
  }
}

function onViewportRightClick(e){
  if(playMode)return;
  e.preventDefault();
  const m=document.getElementById('ctx-menu');
  m.style.left=e.clientX+'px';
  m.style.top=e.clientY+'px';
  m.style.display='block';
  // also try to select
  const rect=renderer.domElement.getBoundingClientRect();
  mouse.x=((e.clientX-rect.left)/rect.width)*2-1;
  mouse.y=-((e.clientY-rect.top)/rect.height)*2+1;
  raycaster.setFromCamera(mouse,camera);
  const meshes=sceneObjects.filter(o=>o.mesh&&o.mesh.isMesh).map(o=>o.mesh);
  const hits=raycaster.intersectObjects(meshes,false);
  if(hits.length>0){
    const sid=hits[0].object.userData.studioId;
    const entry=sceneObjects.find(o=>o.id===sid);
    if(entry)selectObject(entry);
  }
}
function closeCtx(){document.getElementById('ctx-menu').style.display='none';}

// ── Explorer ──────────────────────────
function buildExplorer(){
  const tree=document.getElementById('scene-tree');
  tree.innerHTML='';
  // Workspace root
  const root=document.createElement('div');
  root.className='tree-item';
  root.innerHTML='<span class="tree-icon">&#127758;</span><span>Workspace</span>';
  tree.appendChild(root);
  const children=document.createElement('div');
  children.className='tree-children';
  sceneObjects.forEach(o=>{
    children.appendChild(buildTreeItem(o));
  });
  tree.appendChild(children);
}

function buildTreeItem(entry){
  const div=document.createElement('div');
  const row=document.createElement('div');
  row.className='tree-item'+(selected&&selected.id===entry.id?' selected':'');
  row.innerHTML='<span class="tree-icon">'+(TYPE_ICONS[entry.type]||'&#9642;')+'</span><span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="'+entry.name+'">'+entry.name+'</span>';
  row.addEventListener('click',e=>{e.stopPropagation();selectObject(entry);});
  div.appendChild(row);
  if(entry.children&&entry.children.length){
    const ch=document.createElement('div');ch.className='tree-children';
    entry.children.forEach(c=>ch.appendChild(buildTreeItem(c)));
    div.appendChild(ch);
  }
  return div;
}

// ── Properties Panel ──────────────────
function buildPropsPanel(){
  const body=document.getElementById('props-body');
  if(!selected){body.innerHTML='<div class="no-select">Select an object to edit its properties.</div>';return;}
  const o=selected;
  const p=o.props||{};
  const pos=o.mesh?o.mesh.position:new THREE.Vector3();
  const rot=o.mesh?o.mesh.rotation:new THREE.Euler();
  const sc=o.mesh?o.mesh.scale:new THREE.Vector3(1,1,1);

  let html=`
  <div class="props-section">
    <div class="props-title">Identity</div>
    <div class="prop-row"><span class="prop-label">Name</span><div class="prop-val"><input class="prop-input" id="pn-name" value="${escHtml(o.name)}" onchange="setPropName(this.value)"/></div></div>
    <div class="prop-row"><span class="prop-label">Type</span><div class="prop-val"><input class="prop-input" value="${o.type}" disabled style="opacity:.5;"/></div></div>
  </div>`;

  if(!o.isVirtual){
    html+=`
  <div class="props-section">
    <div class="props-title">Transform</div>
    <div class="prop-row"><span class="prop-label">Position</span><div class="prop-val">
      <input class="prop-input" type="number" id="p-px" value="${r3(pos.x)}" step="0.5" onchange="setProp('px',this.value)"/>
      <input class="prop-input" type="number" id="p-py" value="${r3(pos.y)}" step="0.5" onchange="setProp('py',this.value)"/>
      <input class="prop-input" type="number" id="p-pz" value="${r3(pos.z)}" step="0.5" onchange="setProp('pz',this.value)"/>
    </div></div>
    <div class="prop-row"><span class="prop-label">Rotation</span><div class="prop-val">
      <input class="prop-input" type="number" id="p-rx" value="${r3(THREE.MathUtils.radToDeg(rot.x))}" step="5" onchange="setProp('rx',this.value)"/>
      <input class="prop-input" type="number" id="p-ry" value="${r3(THREE.MathUtils.radToDeg(rot.y))}" step="5" onchange="setProp('ry',this.value)"/>
      <input class="prop-input" type="number" id="p-rz" value="${r3(THREE.MathUtils.radToDeg(rot.z))}" step="5" onchange="setProp('rz',this.value)"/>
    </div></div>
    <div class="prop-row"><span class="prop-label">Scale</span><div class="prop-val">
      <input class="prop-input" type="number" id="p-sx" value="${r3(sc.x)}" step="0.25" min="0.01" onchange="setProp('sx',this.value)"/>
      <input class="prop-input" type="number" id="p-sy" value="${r3(sc.y)}" step="0.25" min="0.01" onchange="setProp('sy',this.value)"/>
      <input class="prop-input" type="number" id="p-sz" value="${r3(sc.z)}" step="0.25" min="0.01" onchange="setProp('sz',this.value)"/>
    </div></div>
  </div>`;
  }

  if(o.mesh&&o.mesh.isMesh&&!o.isVirtual){
    html+=`
  <div class="props-section">
    <div class="props-title">Appearance</div>
    <div class="prop-row"><span class="prop-label">Color</span><div class="prop-val">
      <input type="color" class="prop-color" id="p-color" value="${p.color||'#a78bfa'}" onchange="setProp('color',this.value)"/>
      <input class="prop-input" id="p-colorhex" value="${p.color||'#a78bfa'}" onchange="setProp('color',this.value)" style="flex:1;"/>
    </div></div>
    <div class="prop-row"><span class="prop-label">Roughness</span><div class="prop-val"><div class="slider-wrap">
      <input type="range" class="prop-slider" id="p-rough" min="0" max="1" step="0.05" value="${p.roughness!=null?p.roughness:.7}" onchange="setProp('roughness',this.value)"/>
      <span id="p-rough-val" style="font-size:.7rem;color:var(--muted);min-width:28px;">${r3(p.roughness!=null?p.roughness:.7)}</span>
    </div></div></div>
    <div class="prop-row"><span class="prop-label">Metalness</span><div class="prop-val"><div class="slider-wrap">
      <input type="range" class="prop-slider" id="p-metal" min="0" max="1" step="0.05" value="${p.metalness!=null?p.metalness:.05}" onchange="setProp('metalness',this.value)"/>
      <span id="p-metal-val" style="font-size:.7rem;color:var(--muted);min-width:28px;">${r3(p.metalness!=null?p.metalness:.05)}</span>
    </div></div></div>
  </div>`;
  }

  if(!o.isVirtual){
    html+=`
  <div class="props-section">
    <div class="props-title">Behavior</div>
    <div class="prop-row"><span class="prop-label">Anchored</span><div class="prop-val">
      <label class="prop-toggle"><input type="checkbox" id="p-anch" ${p.anchored?'checked':''} onchange="setProp('anchored',this.checked)"/><span class="toggle-slider"></span></label>
    </div></div>
    <div class="prop-row"><span class="prop-label">CanCollide</span><div class="prop-val">
      <label class="prop-toggle"><input type="checkbox" id="p-col" ${p.canCollide!==false?'checked':''} onchange="setProp('canCollide',this.checked)"/><span class="toggle-slider"></span></label>
    </div></div>
    <div class="prop-row"><span class="prop-label">Visible</span><div class="prop-val">
      <label class="prop-toggle"><input type="checkbox" id="p-vis" ${p.visible!==false?'checked':''} onchange="setProp('visible',this.checked)"/><span class="toggle-slider"></span></label>
    </div></div>
  </div>`;
  }

  if(o.type==='Script'){
    html+=`
  <div class="props-section">
    <div class="props-title">Script</div>
    <div class="prop-row" style="flex-direction:column;align-items:flex-start;gap:6px;padding:8px;">
      <button class="btn btn-primary" style="font-size:.75rem;padding:5px 14px;" onclick="openScriptEditor()">&#128196; Open Script Editor</button>
    </div>
  </div>`;
  }

  body.innerHTML=html;
  // live slider labels
  const roughSlider=document.getElementById('p-rough');
  const metalSlider=document.getElementById('p-metal');
  if(roughSlider) roughSlider.addEventListener('input',()=>{
    document.getElementById('p-rough-val').textContent=r3(roughSlider.value);
  });
  if(metalSlider) metalSlider.addEventListener('input',()=>{
    document.getElementById('p-metal-val').textContent=r3(metalSlider.value);
  });
}

function updatePropsFromMesh(){
  if(!selected||!selected.mesh)return;
  const m=selected.mesh;
  const upd=(id,val)=>{const el=document.getElementById(id);if(el)el.value=val;};
  upd('p-px',r3(m.position.x));
  upd('p-py',r3(m.position.y));
  upd('p-pz',r3(m.position.z));
  upd('p-rx',r3(THREE.MathUtils.radToDeg(m.rotation.x)));
  upd('p-ry',r3(THREE.MathUtils.radToDeg(m.rotation.y)));
  upd('p-rz',r3(THREE.MathUtils.radToDeg(m.rotation.z)));
  upd('p-sx',r3(m.scale.x));
  upd('p-sy',r3(m.scale.y));
  upd('p-sz',r3(m.scale.z));
}

function setPropName(v){
  if(!selected)return;
  selected.name=v;
  buildExplorer();
}

function setProp(key,val){
  if(!selected)return;
  const m=selected.mesh;
  switch(key){
    case'px':m.position.x=parseFloat(val);break;
    case'py':m.position.y=parseFloat(val);break;
    case'pz':m.position.z=parseFloat(val);break;
    case'rx':m.rotation.x=THREE.MathUtils.degToRad(parseFloat(val));break;
    case'ry':m.rotation.y=THREE.MathUtils.degToRad(parseFloat(val));break;
    case'rz':m.rotation.z=THREE.MathUtils.degToRad(parseFloat(val));break;
    case'sx':m.scale.x=Math.max(.01,parseFloat(val));break;
    case'sy':m.scale.y=Math.max(.01,parseFloat(val));break;
    case'sz':m.scale.z=Math.max(.01,parseFloat(val));break;
    case'color':{
      selected.props.color=val;
      if(m.material&&m.material.color)m.material.color.set(val);
      const hex=document.getElementById('p-colorhex');
      const col=document.getElementById('p-color');
      if(hex)hex.value=val;
      if(col)col.value=val;
      break;}
    case'roughness':
      selected.props.roughness=parseFloat(val);
      if(m.material)m.material.roughness=parseFloat(val);
      break;
    case'metalness':
      selected.props.metalness=parseFloat(val);
      if(m.material)m.material.metalness=parseFloat(val);
      break;
    case'anchored':
      selected.props.anchored=val;
      break;
    case'canCollide':
      selected.props.canCollide=val;
      break;
    case'visible':
      selected.props.visible=val;
      m.visible=val;
      break;
  }
  pushUndo();
}

function r3(n){return Math.round(parseFloat(n)*1000)/1000;}
function escHtml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}

// ── Script Editor ─────────────────────
function openScriptEditor(){
  if(!selected||selected.type!=='Script')return;
  document.getElementById('script-editor-name').textContent=selected.name;
  document.getElementById('code-input').value=selected.script||'';
  document.getElementById('tab-props').classList.add('hidden');
  document.getElementById('script-editor').style.display='flex';
  updateLineNumbers();
  // switch right tab
  document.querySelectorAll('#right-panel .panel-tab').forEach((t,i)=>{
    t.classList.toggle('active',i===1);
  });
}
function closeScriptEditor(){
  if(selected&&selected.type==='Script'){
    selected.script=document.getElementById('code-input').value;
  }
  document.getElementById('script-editor').style.display='none';
  document.getElementById('tab-props').classList.remove('hidden');
  document.querySelectorAll('#right-panel .panel-tab').forEach((t,i)=>{
    t.classList.toggle('active',i===0);
  });
}
document.getElementById('code-input').addEventListener('input',updateLineNumbers);
document.getElementById('code-input').addEventListener('keydown',e=>{
  if(e.key==='Tab'){e.preventDefault();const ta=e.target;const s=ta.selectionStart,en=ta.selectionEnd;ta.value=ta.value.substring(0,s)+'  '+ta.value.substring(en);ta.selectionStart=ta.selectionEnd=s+2;updateLineNumbers();}
});
function updateLineNumbers(){
  const ta=document.getElementById('code-input');
  const lines=ta.value.split('\n').length;
  document.getElementById('line-numbers').innerHTML=Array.from({length:lines},(_,i)=>i+1).join('<br>');
}

// ── Toolbox ───────────────────────────
const TOOLBOX_ITEMS=[
  {type:'Part',icon:'&#9646;',label:'Part'},
  {type:'Sphere',icon:'&#9711;',label:'Sphere'},
  {type:'Cylinder',icon:'&#11618;',label:'Cylinder'},
  {type:'Wedge',icon:'&#11176;',label:'Wedge'},
  {type:'Torus',icon:'&#9737;',label:'Torus'},
  {type:'Cone',icon:'&#9651;',label:'Cone'},
  {type:'Spawn',icon:'&#9654;',label:'Spawn'},
  {type:'PointLight',icon:'&#9728;',label:'Point Light'},
  {type:'SpotLight',icon:'&#9681;',label:'Spot Light'},
  {type:'Script',icon:'&#128196;',label:'Script'},
  {type:'Model',icon:'&#128194;',label:'Model'},
];
function buildToolbox(){
  const g=document.getElementById('toolbox-grid');
  g.innerHTML='';
  TOOLBOX_ITEMS.forEach(item=>{
    const d=document.createElement('div');
    d.className='tool-card';
    d.innerHTML='<span class="tool-icon">'+item.icon+'</span><span>'+item.label+'</span>';
    d.onclick=()=>insertObject(item.type);
    g.appendChild(d);
  });
}

// ── Undo/Redo ─────────────────────────
function captureState(){
  return sceneObjects.map(o=>({
    id:o.id,
    pos:o.mesh?o.mesh.position.clone():null,
    rot:o.mesh?o.mesh.rotation.clone():null,
    sc:o.mesh?o.mesh.scale.clone():null,
    vis:o.props?o.props.visible:true
  }));
}
function pushUndo(){
  undoStack.push(captureState());
  if(undoStack.length>MAX_UNDO)undoStack.shift();
  redoStack.length=0;
}
function applyState(state){
  state.forEach(s=>{
    const o=sceneObjects.find(x=>x.id===s.id);
    if(o&&o.mesh){
      if(s.pos)o.mesh.position.copy(s.pos);
      if(s.rot)o.mesh.rotation.copy(s.rot);
      if(s.sc)o.mesh.scale.copy(s.sc);
      if(o.props)o.props.visible=s.vis;
      o.mesh.visible=s.vis;
    }
  });
  buildPropsPanel();
  if(selected) updatePropsFromMesh();
}
function undo(){
  if(!undoStack.length)return;
  redoStack.push(captureState());
  applyState(undoStack.pop());
  conLog('Undo','info');
}
function redo(){
  if(!redoStack.length)return;
  undoStack.push(captureState());
  applyState(redoStack.pop());
  conLog('Redo','info');
}

// ── Delete / Duplicate / Copy ─────────
function deleteSelected(){
  if(!selected)return;
  if(selected.isBasePlate){conLog('Cannot delete Baseplate','warn');return;}
  scene.remove(selected.mesh);
  sceneObjects=sceneObjects.filter(o=>o.id!==selected.id);
  transformControls.detach();
  selected=null;
  buildExplorer();
  buildPropsPanel();
  pushUndo();
  conLog('Object deleted','info');
}
function copyObj(){
  if(!selected)clipboard=null;
  else clipboard=selected;
  conLog('Copied: '+(selected?selected.name:'nothing'),'info');
}
function cutObj(){
  copyObj();
  deleteSelected();
}
function pasteObj(){
  if(!clipboard)return;
  duplicateEntry(clipboard);
}
function duplicateObj(){
  if(!selected)return;
  duplicateEntry(selected);
}
function duplicateEntry(entry){
  if(!entry.mesh)return;
  const newPos=entry.mesh.position.clone().add(new THREE.Vector3(2,0,0));
  insertObject(entry.type,newPos);
  // copy color
  if(entry.props&&entry.props.color&&selected){
    selected.props.color=entry.props.color;
    if(selected.mesh.material)selected.mesh.material.color.set(entry.props.color);
  }
  conLog('Duplicated: '+entry.name,'info');
}

// ── Camera controls ───────────────────
function focusSelected(){
  if(!selected||!selected.mesh)return;
  const pos=selected.mesh.position;
  const offset=new THREE.Vector3(5,4,7);
  camera.position.copy(pos).add(offset);
  orbitControls.target.copy(pos);
  orbitControls.update();
}
function resetCamera(){
  camera.position.set(18,14,22);
  orbitControls.target.set(0,0,0);
  orbitControls.update();
}
function toggleGrid(){
  gridHelper.visible=!gridHelper.visible;
}
function toggleWireframe(){
  wireframeMode=!wireframeMode;
  sceneObjects.forEach(o=>{
    if(o.mesh&&o.mesh.material&&!o.isVirtual){
      if(Array.isArray(o.mesh.material))o.mesh.material.forEach(m=>m.wireframe=wireframeMode);
      else o.mesh.material.wireframe=wireframeMode;
    }
  });
}

// ── Scene / Save ─────────────────────
function newScene(){
  if(!confirm('Create a new scene? Unsaved changes will be lost.'))return;
  sceneObjects.filter(o=>!o.isBasePlate).forEach(o=>scene.remove(o.mesh));
  sceneObjects=sceneObjects.filter(o=>o.isBasePlate);
  _nameCounters={};
  deselectAll();
  buildExplorer();
  conLog('New scene created','ok');
}
function saveScene(){
  const data={
    objects:sceneObjects.filter(o=>!o.isBasePlate).map(o=>({
      id:o.id,name:o.name,type:o.type,
      pos:o.mesh?{x:o.mesh.position.x,y:o.mesh.position.y,z:o.mesh.position.z}:null,
      rot:o.mesh?{x:o.mesh.rotation.x,y:o.mesh.rotation.y,z:o.mesh.rotation.z}:null,
      sc:o.mesh?{x:o.mesh.scale.x,y:o.mesh.scale.y,z:o.mesh.scale.z}:null,
      props:o.props,script:o.script||null
    })),
    savedAt:Date.now()
  };
  localStorage.setItem('eylox_studio_scene',JSON.stringify(data));
  conLog('Scene saved to localStorage','ok');
}
function exportHTML(){
  const blob=new Blob([document.documentElement.outerHTML],{type:'text/html'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download='eylox-studio.html';
  a.click();
  conLog('Exported HTML file','ok');
}
function publishGame(){
  const name=prompt('Game name:','My Eylox Game');
  if(!name)return;
  const games=JSON.parse(localStorage.getItem('eylox_my_games')||'[]');
  const entry={id:'game_'+Date.now(),name,author:localStorage.getItem('eylox_user')||'Guest',createdAt:Date.now(),objectCount:sceneObjects.length};
  games.push(entry);
  localStorage.setItem('eylox_my_games',JSON.stringify(games));
  conLog('Game "'+name+'" published!','ok');
  alert('Game published! Check My Games in the home page.');
}

// ── Play Mode ────────────────────────
function startPlay(){
  if(playMode)return;
  playMode=true;
  document.getElementById('play-btn').style.display='none';
  document.getElementById('stop-btn').style.display='inline-flex';
  document.getElementById('vp-badge').style.display='block';
  orbitControls.enabled=false;
  transformControls.detach();
  deselectAll();

  // save camera
  editCamPos.copy(camera.position);
  editCamTarget.copy(orbitControls.target);

  // spawn player
  const spawnEntry=sceneObjects.find(o=>o.type==='Spawn');
  const spawnPos=spawnEntry?spawnEntry.mesh.position.clone():new THREE.Vector3(0,3,0);
  spawnPos.y+=2;

  const capsGeo=new THREE.CapsuleGeometry?new THREE.CapsuleGeometry(.5,1.5,8,16):new THREE.CylinderGeometry(.5,.5,2,16);
  const capsMat=new THREE.MeshStandardMaterial({color:0xa78bfa,roughness:.5,metalness:.1});
  playerObj=new THREE.Mesh(capsGeo,capsMat);
  playerObj.position.copy(spawnPos);
  playerObj.castShadow=true;
  scene.add(playerObj);
  playerVel.set(0,0,0);
  playerOnGround=false;
  playerPitch=0;
  playerYaw=0;

  // pointer lock
  renderer.domElement.requestPointerLock();
  renderer.domElement.addEventListener('mousemove',onPlayerMouseMove);
  conLog('Play mode started. WASD to move, Space to jump, Esc to stop.','ok');
}

function stopPlay(){
  if(!playMode)return;
  playMode=false;
  document.getElementById('play-btn').style.display='inline-flex';
  document.getElementById('stop-btn').style.display='none';
  document.getElementById('vp-badge').style.display='none';
  orbitControls.enabled=true;

  if(playerObj){scene.remove(playerObj);playerObj=null;}
  if(document.pointerLockElement)document.exitPointerLock();
  renderer.domElement.removeEventListener('mousemove',onPlayerMouseMove);

  camera.position.copy(editCamPos);
  orbitControls.target.copy(editCamTarget);
  orbitControls.update();
  conLog('Play mode stopped','info');
}

function onPlayerMouseMove(e){
  if(!pointerLocked||!playMode)return;
  const sens=0.002;
  playerYaw-=e.movementX*sens;
  playerPitch-=e.movementY*sens;
  playerPitch=Math.max(-Math.PI/2.5,Math.min(Math.PI/2.5,playerPitch));
}

function updatePlayer(dt){
  if(!playerObj)return;
  const gravity=-20;
  const speed=8;
  const jumpForce=9;

  // gravity
  playerVel.y+=gravity*dt;

  // ground check (simple: y>0.5)
  const groundY=0.1; // just above baseplate top
  if(playerObj.position.y<=groundY+1){
    playerObj.position.y=groundY+1;
    if(playerVel.y<0){playerVel.y=0;playerOnGround=true;}
  } else {
    playerOnGround=false;
  }

  // movement
  const fwd=new THREE.Vector3(Math.sin(playerYaw),0,Math.cos(playerYaw));
  const right=new THREE.Vector3(Math.cos(playerYaw),0,-Math.sin(playerYaw));
  const move=new THREE.Vector3();
  if(keysHeld['KeyW']||keysHeld['ArrowUp'])move.sub(fwd);
  if(keysHeld['KeyS']||keysHeld['ArrowDown'])move.add(fwd);
  if(keysHeld['KeyA']||keysHeld['ArrowLeft'])move.sub(right);
  if(keysHeld['KeyD']||keysHeld['ArrowRight'])move.add(right);
  if(move.lengthSq()>0)move.normalize().multiplyScalar(speed);
  playerVel.x=move.x;
  playerVel.z=move.z;

  if((keysHeld['Space'])&&playerOnGround){
    playerVel.y=jumpForce;
    playerOnGround=false;
  }

  playerObj.position.addScaledVector(playerVel,dt);

  // camera follow
  const camOffset=new THREE.Vector3(
    Math.sin(playerYaw)*4,
    2.5,
    Math.cos(playerYaw)*4
  );
  camera.position.copy(playerObj.position).add(camOffset);
  const lookAt=playerObj.position.clone().add(new THREE.Vector3(
    -Math.sin(playerYaw)*2,
    playerPitch*3,
    -Math.cos(playerYaw)*2
  ));
  camera.lookAt(lookAt);
}

// ── Keyboard Shortcuts ────────────────
function onKeyDown(e){
  keysHeld[e.code]=true;
  if(playMode){
    if(e.key==='F6'||e.key==='Escape'){stopPlay();}
    return;
  }
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'||e.target.tagName==='SELECT')return;
  if(e.key==='F5'){e.preventDefault();startPlay();return;}
  if(e.key==='F6'){e.preventDefault();stopPlay();return;}
  if(e.ctrlKey||e.metaKey){
    switch(e.key.toLowerCase()){
      case'z':e.preventDefault();undo();break;
      case'y':e.preventDefault();redo();break;
      case's':e.preventDefault();saveScene();break;
      case'd':e.preventDefault();duplicateObj();break;
      case'c':e.preventDefault();copyObj();break;
      case'v':e.preventDefault();pasteObj();break;
      case'x':e.preventDefault();cutObj();break;
    }
    return;
  }
  switch(e.key.toLowerCase()){
    case'q':setTool('select');break;
    case'w':setTool('move');break;
    case'e':setTool('scale');break;
    case'r':setTool('rotate');break;
    case'f':focusSelected();break;
    case'g':toggleGrid();break;
    case'delete':case'backspace':deleteSelected();break;
  }
}

function onMouseMove(e){
  if(playMode)return;
  const rect=renderer.domElement.getBoundingClientRect();
  mouse.x=((e.clientX-rect.left)/rect.width)*2-1;
  mouse.y=-((e.clientY-rect.top)/rect.height)*2+1;
}

// ── Menu helpers ──────────────────────
function toggleMenu(id){
  const dd=document.getElementById(id);
  const wasOpen=dd.classList.contains('open');
  closeMenus();
  if(!wasOpen)dd.classList.add('open');
}
function closeMenus(){
  document.querySelectorAll('.dropdown').forEach(d=>d.classList.remove('open'));
}

// ── Tab switchers ─────────────────────
function switchLeftTab(tab,btn){
  document.querySelectorAll('#left-panel .panel-tab').forEach(t=>t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('tab-explorer').classList.toggle('hidden',tab!=='explorer');
  document.getElementById('tab-toolbox').classList.toggle('hidden',tab!=='toolbox');
}
function switchRightTab(tab,btn){
  document.querySelectorAll('#right-panel .panel-tab').forEach(t=>t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('tab-props').classList.toggle('hidden',tab!=='props');
  const se=document.getElementById('script-editor');
  if(tab==='script'){
    if(selected&&selected.type==='Script'){openScriptEditor();}
    else{se.style.display='none';document.getElementById('tab-props').classList.remove('hidden');btn.classList.remove('active');document.querySelectorAll('#right-panel .panel-tab')[0].classList.add('active');}
  } else {
    se.style.display='none';
    document.getElementById('tab-props').classList.remove('hidden');
  }
}
function switchBottomTab(tab,btn){
  document.querySelectorAll('.bottom-tab').forEach(t=>t.classList.remove('active'));
  btn.classList.add('active');
}
function togglePanel(id){
  const p=document.getElementById(id);
  p.style.display=p.style.display==='none'?'':'none';
}

// ── Console ───────────────────────────
function conLog(msg,type='info'){
  const out=document.getElementById('console-output');
  const line=document.createElement('div');
  line.className='con-line con-'+type;
  const time=new Date().toLocaleTimeString('en',{hour12:false,hour:'2-digit',minute:'2-digit',second:'2-digit'});
  line.textContent='['+time+'] '+msg;
  out.appendChild(line);
  out.scrollTop=out.scrollHeight;
}

// ── Window resize ─────────────────────
window.addEventListener('resize',()=>{
  resizeRenderer();
  setTimeout(resizeRenderer,100);
});

// ── Login enter key ───────────────────
document.getElementById('li-user').addEventListener('keydown',e=>{
  if(e.key==='Enter')document.getElementById('li-pass').focus();
});
</script>
</body>
</html>
"""

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

size_bytes = os.path.getsize(output_path)
size_kb = size_bytes / 1024
print(f"Written: {output_path}")
print(f"Size: {size_kb:.2f} KB ({size_bytes} bytes)")
