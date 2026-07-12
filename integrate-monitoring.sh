#!/bin/bash
# ============================================================
# EYLOX Platform — Automated Error Handling & Monitoring Integration
# Injects error auditor, recovery, and performance monitoring into all HTML files
# ============================================================

EYLOX_DIR="c:/Users/ip/Desktop/EYLOX/Eylox WEB html"

echo "🔧 Integrating error handling & monitoring systems..."

# HTML header snippet to add (right before closing </head>)
MONITORING_SNIPPET='<!-- EYLOX Error Handling & Performance Monitoring -->
<script src="error-auditor.js"></script>
<script src="error-recovery.js"></script>
<script src="perf-monitor.js"></script>'

# Function to integrate into HTML file
integrate_html() {
  local file=$1
  local filename=$(basename "$file")

  # Skip files that already have monitoring
  if grep -q "error-auditor.js" "$file" 2>/dev/null; then
    echo "  ✓ Already integrated: $filename"
    return
  fi

  # Add scripts before </head>
  if grep -q "</head>" "$file"; then
    sed -i "s|</head>|$MONITORING_SNIPPET\n</head>|g" "$file"
    echo "  ✓ Integrated into: $filename"
  else
    echo "  ⚠️ No </head> tag in: $filename (skip)"
  fi
}

# Process all HTML files
echo ""
echo "📄 Processing HTML files..."
find "$EYLOX_DIR" -maxdepth 1 -name "*.html" -type f | while read file; do
  integrate_html "$file"
done

echo ""
echo "✅ Integration complete!"
echo ""
echo "📊 Monitoring now enabled on all pages:"
echo "   • Error Auditor: Validates all DOM elements, buttons, links"
echo "   • Error Recovery: Catches and recovers from failures"
echo "   • Performance Monitor: Tracks FPS, memory, load times"
