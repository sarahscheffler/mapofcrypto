# Specification (currently more of a brainstorm)

### Latest changes
* 2018/05/11. SS.  Initial commit.  Added initial list of protocols to include, 
  link types, categories, etc.

### TODO
* Assign UIDs to everything
* Figure out which of these things below should be "objects" or "classes" and 
  which should be "interfaces" or "types" or "attributes" or whatever.
* Provide a way to attach a proof/construction.
* Start defining links (with blowup factors!)

## Link types
* "X is a type of Y (all X are Y)"
* "ø¸¨¢ƒ asdf asdf"
* "$\exists$ X implies $\exists$ Y"
* "$\exists$ X implies $\neg \exists$ Y"
* "$\exists$ X does NOT imply $\exists$ Y"
* "X can be used as a building block (along with Z1 and Z2) for Y"
* [Links also need to include a way to have a growth factor (e.g. you can build
  Y out of X at $O(n^2)$ cost)]

## Entities
### Primitives
* PRGs
* PRFs
    * Constrained PRFs
* OWFs
    * Strong
    * Weak
    * OWPs
    * Trapdoor OWPs (are these different?)
    * Universal OWF
    * Hard core predicates
* OT
    * 2-SH-OT
    * k-SH-OT
* KA
    * 2-KA
    * (k-1)-KA
    * k-KA
* KE
* CR functions (not sure where to put?)
* $t$-wise indep fns
* Universal HF

### Objects
* Block Ciphers
* Hash Functions

### Types of Schemes
* PKE
* Signature Scheme
* Symmetric key encryption
* Message Authentication Codes
* FE
* IBE
* ABE
* Commitments

### Definitions
* IND-CPA
* IND-CCA
* NM-CCA
* EU-CMA

### Proof things
* PoK
* IP
* ZK
    * Constant round
    * NIZK
    * SNARKs
* WI

### Assumptions
* DDH
* CDH
* ROM

### Obfuscation stuff (to classify)
* VBB
* VGB
* iO

### Guarantees
* Confidentiality
* Integrity
* Deniability
* ZK
* Forward Secrecy
* Repubidability
* Non-repudiability

### Types 
* Minicrypt vs Cryptomania
* Symmetric vs PK



