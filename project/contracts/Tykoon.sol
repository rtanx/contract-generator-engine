// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "chiru-labs/ERC721A@4.2.3/contracts/ERC721A.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.3/contracts/access/Ownable.sol";

contract Tykoon is ERC721A, Ownable {
    string private _baseTokenURI;

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _baseuri
    ) ERC721A(_name, _symbol) {
        _baseTokenURI = _baseuri;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory _baseuri) public onlyOwner {
        _baseTokenURI = _baseuri;
    }

    function safeMint(uint256 quantity) external payable {
        _safeMint(msg.sender, quantity);
    }
}
