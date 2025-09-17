#!/usr/bin/env python3
"""
测试安全配置管理功能
"""

import os
import sys
from config_manager import get_secure_config

def test_config_manager():
    """测试配置管理器功能"""
    print("=== 测试安全配置管理器 ===")
    
    try:
        # 创建配置管理器实例
        config_manager = get_secure_config("config_secure.yaml")
        
        # 测试获取API密钥
        print("\n1. 获取API密钥:")
        api_keys = config_manager.get_api_keys()
        for key, value in api_keys.items():
            if value:
                print(f"   {key}: {'*' * (len(value) - 4) + value[-4:]}")
            else:
                print(f"   {key}: [未设置]")
        
        # 测试验证API密钥
        print("\n2. 验证API密钥:")
        validation_results = config_manager.validate_api_keys()
        for key, is_valid in validation_results.items():
            status = "✓ 有效" if is_valid else "✗ 无效/缺失"
            print(f"   {key}: {status}")
        
        # 测试获取缺失的密钥
        print("\n3. 缺失的API密钥:")
        missing_keys = config_manager.get_missing_keys()
        if missing_keys:
            for key in missing_keys:
                print(f"   - {key}")
        else:
            print("   所有API密钥都已配置")
        
        # 测试创建环境变量模板
        print("\n4. 创建环境变量模板:")
        config_manager.create_env_template(".env.test")
        if os.path.exists(".env.test"):
            print("   ✓ 环境变量模板创建成功")
            os.remove(".env.test")  # 清理测试文件
        else:
            print("   ✗ 环境变量模板创建失败")
        
        print("\n=== 测试完成 ===")
        return True
        
    except Exception as e:
        print(f"测试失败: {e}")
        return False

def test_agent_integration():
    """测试与Agent的集成"""
    print("\n=== 测试Agent集成 ===")
    
    try:
        # 导入更新后的Agent
        from agent_updated import MusicAgent
        
        # 创建Agent实例
        agent = MusicAgent("config_secure.yaml", mode="cli")
        
        # 测试获取API状态
        print("\n1. 获取API状态:")
        status = agent.get_api_status()
        print(f"   验证结果: {status['validation_results']}")
        print(f"   缺失密钥: {status['missing_keys']}")
        
        print("\n=== Agent集成测试完成 ===")
        return True
        
    except Exception as e:
        print(f"Agent集成测试失败: {e}")
        return False

if __name__ == "__main__":
    print("Emind 安全配置测试")
    print("=" * 50)
    
    # 运行测试
    config_test_passed = test_config_manager()
    agent_test_passed = test_agent_integration()
    
    # 总结
    print("\n" + "=" * 50)
    print("测试总结:")
    print(f"配置管理器测试: {'通过' if config_test_passed else '失败'}")
    print(f"Agent集成测试: {'通过' if agent_test_passed else '失败'}")
    
    if config_test_passed and agent_test_passed:
        print("\n✓ 所有测试通过！安全配置系统工作正常。")
        sys.exit(0)
    else:
        print("\n✗ 部分测试失败，请检查配置。")
        sys.exit(1)
