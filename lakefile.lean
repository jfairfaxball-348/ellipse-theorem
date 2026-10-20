import Lake
open Lake DSL

package «ETSHTS» where

-- Mathlib v4.35.0-rc3 release commit, paired with the Lean v4.35.0-rc3 toolchain.
require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "c55e6e786f49471c72fbddbec5415808896aec1e"

@[default_target]
lean_lib ETSHTS where

-- Palomar independent statement/proof module surfaces; neither is the default build target.
lean_lib Challenge where

lean_lib Solution where
