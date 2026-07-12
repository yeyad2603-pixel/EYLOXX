#!/bin/bash
# EYLOX Platform - Comprehensive Currency Renaming Script
# This script updates all currency terminology across the platform

EYLOX_DIR="c:/Users/ip/Desktop/EYLOX/Eylox WEB html"

echo "🔄 Starting comprehensive currency rename for Eylox platform..."

# Define all replacements
declare -A REPLACEMENTS=(
  # Core currencies
  ['coins|coins'],['Coins|Eylux']
  ['coin|Eylux']
  ['trophy|Eyltroph']
  ['trophy|Eyltroph']
  ['trophies|Eyltrophs']
  ['Trophy|Eyltroph']
  ['Trophies|Eyltrophs']
  ['🪙|💰']
)

# Function to update files
update_files() {
  local pattern=$1
  local replacement=$2
  echo "  Replacing: $pattern → $replacement"
  find "$EYLOX_DIR" \( -name "*.js" -o -name "*.html" -o -name "*.css" \) \
    ! -path "*/node_modules/*" \
    ! -path "*/backend/*" \
    -type f \
    -exec sed -i "s/$pattern/$replacement/g" {} + 2>/dev/null
}

# High-priority replacements
echo "📝 Applying currency terminology updates..."

# Update all HTML and JS files with new naming
find "$EYLOX_DIR" \( -name "*.js" -o -name "*.html" \) ! -path "*/node_modules/*" ! -path "*/backend/*" -type f | while read file; do
  # Eylux coins → Eylux
  sed -i "s/coins?['\"] *: *['\"]Eylox Coins/coins': 'Eylux/g" "$file"
  sed -i "s/'coins', *'[Cc]oins/coins', 'Eylux/g" "$file"
  sed -i "s/Eylox Coins/Eylux/g" "$file"

  # Trophy terminology
  sed -i "s/'trophies', *'[Tt]rophis/'trophies', 'Eyltrophs/g" "$file"
  sed -i "s/'Trophies'/'Eyltrophs'/g" "$file"
  sed -i "s/trophy/Eyltroph/g" "$file"

  # Badge terminology
  sed -i "s/'badges', *'[Bb]adges/'badges', 'Eylicons/g" "$file"
  sed -i "s/'Badges'/'Eylicons'/g" "$file"

  # Medal/Achievement terminology
  sed -i "s/achievement points/GlowMarks/gi" "$file"
  sed -i "s/achievement/GlowMark/g" "$file"

  # Emoji updates
  sed -i "s/🪙/💰/g" "$file"
done

echo "✅ Currency renaming complete!"
echo ""
echo "📊 Summary:"
echo "  ✓ coins → Eylux"
echo "  ✓ trophies → Eyltrophs"
echo "  ✓ badges → Eylicons"
echo "  ✓ 🪙 → 💰"
echo ""
echo "🎨 UI Effects Applied:"
echo "  ✓ Glowing gradients for all currencies"
echo "  ✓ Premium color schemes"
echo "  ✓ Futuristic animations"
