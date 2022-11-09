// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "chiru-labs/ERC721A@4.2.3/contracts/ERC721A.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.3/contracts/access/Ownable.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.3/contracts/token/ERC20/IERC20.sol";

contract Tykoon is ERC721A, Ownable {
    IERC20 public idrt;

    string private _baseTokenURI;
    uint256 private _maxSupply;
    uint256 private _idrtPricePerNFT;

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _baseuri,
        uint256 _maxsupply,
        uint256 _nftPriceInIdrt,
        address _idrtAddress
    ) ERC721A(_name, _symbol) {
        _baseTokenURI = _baseuri;
        _maxSupply = _maxsupply;
        _idrtPricePerNFT = _nftPriceInIdrt;
        idrt = IERC20(_idrtAddress);
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory _baseuri) public onlyOwner {
        _baseTokenURI = _baseuri;
    }

    function safeMint(uint256 quantity) external {
        require(
            totalSupply() + quantity <= _maxSupply,
            "Not enough NFTs to mint, reached maximum supply"
        );
        bool tfSucceed = idrt.transferFrom(
            msg.sender,
            address(this),
            quantity * _idrtPricePerNFT
        );
        require(tfSucceed, "Failed to make USDT transfer transaction");
        _safeMint(msg.sender, quantity);
    }

    function withdrawIDRT(uint256 amount, address to) external onlyOwner {
        idrt.transferFrom(address(this), to, amount);
    }
}
