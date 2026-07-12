#!/usr/bin/env python3
import re

# Read the original file
with open("Eylox WEB html\\eylox-studio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find locations
titlebar_section = '''  <!-- TITLE BAR -->
  <div id="titlebar">
    <div class="tb-left">
      <span class="tb-logo">⬡ EYLOX STUDIO</span>
      <div class="tb-game"><span>My Game</span><span>▾</span></div>
      <button class="tb-icon">+</button><button class="tb-icon">?</button>
    </div>
    <div class="tb-right">
      <button class="tb-collaborate">Collaborate</button>
      <div class="tb-avatar" id="menu-user-label">E</div>
    </div>
  </div>

  <!-- RIBBON TABS -->
  <div id="ribbon-tabs">
    <button class="rtab" onclick="setRibbonTab('file')">FILE</button>
    <button class="rtab active" onclick="setRibbonTab('home')">HOME</button>
    <button class="rtab" onclick="setRibbonTab('model')">MODEL</button>
    <button class="rtab" onclick="setRibbonTab('terrain')">TERRAIN</button>
    <button class="rtab" onclick="setRibbonTab('test')">TEST</button>
    <button class="rtab" onclick="setRibbonTab('view')">VIEW</button>
    <button class="rtab" onclick="setRibbonTab('plugins')">PLUGINS</button>
    <button class="rtab" onclick="setRibbonTab('script')">SCRIPT</button>
  </div>

  <!-- RIBBON TOOLBAR -->
  <div id="ribbon-toolbar">
    <div class="rtoolbar" id="rt-home">
      <div class="rt-group">
        <button class="rt-btn active" id="tb-select" onclick="setTool('select')"><span class="rt-icon">▶</span><span class="rt-label">Select</span></button>
        <button class="rt-btn" id="tb-move" onclick="setTool('move')"><span class="rt-icon">✤</span><span class="rt-label">Move</span></button>
        <button class="rt-btn" id="tb-scale" onclick="setTool('scale')"><span class="rt-icon">⤡</span><span class="rt-label">Scale</span></button>
        <button class="rt-btn" id="tb-rotate" onclick="setTool('rotate')"><span class="rt-icon">↻</span><span class="rt-label">Rotate</span></button>
      </div>
      <div class="rt-group" style="border-right:none;"></div>
    </div>
    <div class="rtoolbar hidden" id="rt-terrain"></div>
  </div>
'''

# Replace the menubar and toolbar section with titlebar + ribbon
menubar_start = content.find('  <!-- MENUBAR -->')
menubar_end = content.find('  <!-- MAIN -->')

content = content[:menubar_start] + titlebar_section + '\n  <!-- MAIN -->' + content[menubar_end+len('  <!-- MAIN -->'):]

# Write back
with open("Eylox WEB html\\eylox-studio.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Eylox Studio updated with Roblox-style ribbon interface!")
