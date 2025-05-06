from dependency_injector import containers, providers
from src.domain.dice import Dice
from src.application.interfaces.dice import DiceService
from src.application.services.dice import DiceServiceImpl

class Container(containers.DeclarativeContainer):
    """依存性注入のコンテナ"""
    
    # 設定
    config = providers.Configuration()
    
    # ドメインオブジェクト
    dice = providers.Singleton(Dice)
    
    # サービス
    dice_service = providers.Singleton(
        DiceServiceImpl,
        dice=dice
    )
    
    def wire(self, packages=None):
        """依存性の注入を設定する"""
        super().wire(packages=packages)
    
    def unwire(self):
        """依存性の注入を解除する"""
        super().unwire()
    
    def init_resources(self):
        """リソースを初期化する"""
        super().init_resources()
    
    def shutdown_resources(self):
        """リソースをシャットダウンする"""
        super().shutdown_resources()
    
    def reset_singletons(self):
        """シングルトンインスタンスをリセットする"""
        self.dice.reset()
        self.dice_service.reset() 