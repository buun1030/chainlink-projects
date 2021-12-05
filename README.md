Contracts

    SimpleStorage.sol
        struct People { favoriteNumber; name }
        function store(_favoriteNumber) public
        function retrieve() public view returns (favoriteNumber)
        function addPerson(_name, _favoriteNumber) public

    FundMe.sol
        import AggregatorV3Interface.sol
        AggregatorV3Interface public priceFeed
        constructor(address _priceFeed) public { priceFeed; owner }
        function fund() public payable
        function getVersion() public view returns (priceFeed.version())
        function getPrice() public view returns (priceFeed.latestRoundData(2nd_output))
        function getConversionRate(ethAmountInUsd)
        function getEntranceFee() public view returns (defined)
        modifier onlyOwner()
        function withdraw() public payable onlyOwner
    
    AggregatorV3Interface.sol
        function getRoundData(_roundId)
        function latestRoundData()

    MockV3Aggregator.sol
        function updateRoundData(multiInput)
        function getRoundData(_roundId) returns (multiOutput)
        function latestRoundData() returns (multiOutput)

    Lottery.sol
        import AggregatorV3Interface.sol
        import Ownable.sol
        import VRFConsumerBase.sol
        AggregatorV3Interface internal ethUsdPriceFeed
        enum LOTTERY_STATE { OPEN, CLOSED, CALCULATING_WINNER }
        constructor (multiInput) public VRFConsumerBase (
            usdEntryFee; ethUsdPriceFeed; lottery_state; fee; keyhash;
        )
        function enter() public payable
        function getEntranceFee() public view returns (costToEnter)
        function startLottery() public onlyOwner
        function endLottery() public onlyOwner
            emit requestRandomness(keyhash, fee)
        function fulfillRandomness(_requestId, _randomness)

Scripts

    deploy.py: version simple_storage_wo_brownie
        read: SimpleStorage.sol
        compile: SimpleStorage.sol
            get: abi, bytecode
        connect: web3 https
            use: chain_id, my_address, private_key
        create contract:
            use: abi, bytecode
            get: nonce, transaction
            sign transaction:
                use: transaction, private_key
                get: hash, receipt
        work with contract:
            deploy contract:
                use: abi, address
                get: contract item
            store value:
                use: contract item
                get: nonce, transaction
            sign transaction:
                use: transaction, private_key
                get: hash, receipt
        call retrieve

    deploy.py: version simple_storage
        import SimpleStorage.sol
        get account:
            use: private_key
        deploy contract:
            use: account
            get: contract item
        store value:
            use: contract item
            get: nonce, transaction
        call retrieve

    deploy.py: version fund_me
        import FundMe.sol
        import MockV3Aggregator.sol
        get account:
            use: private_key
        deploy contract:
            use: account, eth_data_feed
            get: contract item and verify
        fund to contract
        withdraw from contract

    deploy.py: version lottery
        import lottery.sol
        get account:
            use: private_key
        deploy contract:
            use: depend on constructor items in contract
            get: contract item and verify

Tests

    deploy contract
    store value
    fund
    withdraw