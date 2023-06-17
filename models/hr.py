from sqlalchemy import literal_column
from sqlalchemy.dialects.mssql import VARCHAR
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer
from typing import Any, Dict

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import inspect


@as_declarative()
class SqlAlchemyBase:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def dict(self) -> Dict[str, Any]:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class ResignedEmployeeBase:
    """离职表基类"""

    ryid = Column(VARCHAR(100), primary_key=True, comment="人员id")
    per_gh = Column(VARCHAR(100), comment="工号")
    per_xm = Column(VARCHAR(100), comment="姓名")
    per_sfzh = Column(VARCHAR(50), comment="身份证号")
    per_lzrq = Column(DateTime, comment="入职日期")
    per_outrq = Column(DateTime, comment="离职日期")
    per_outfs = Column(VARCHAR(100), comment="离职方式")
    per_jxfs = Column(VARCHAR(100), comment="计薪方式")
    int_zhiji = Column(VARCHAR(50), comment="职级数")
    per_zw = Column(VARCHAR(50), comment="职位")
    syb_id = Column(VARCHAR(100), comment="事业部id")
    per_syb = Column(VARCHAR(100), comment="事业部")
    dpt_id = Column(VARCHAR(100), comment="厂别id")
    per_dpt = Column(VARCHAR(100), comment="厂别")
    zhu_id = Column(VARCHAR(100), comment="部门id")
    per_zhu = Column(VARCHAR(100), comment="部门")


class ResignedEmployeeBaishiPO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_bs"
    __table_args__ = {"comment": "白石园区离职表"}

    base = literal_column("'白石园区'").label("base")


class ResignedEmployeeJingmiPO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_jm"
    __table_args__ = {"comment": "精密园区离职表"}

    base = literal_column("'精密园区'").label("base")


class ResignedEmployeeGaoxinPO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_gx"
    __table_args__ = {"comment": "高新园区离职表"}

    base = literal_column("'高新园区'").label("base")


class ResignedEmployeeMetalPO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_jsc"
    __table_args__ = {"comment": "金属厂园区离职表"}

    base = literal_column("'高新金属厂'").label("base")


class ResignedEmployeeFuxingPO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_fx"
    __table_args__ = {"comment": "伯恩富兴离职表"}

    base = literal_column("'伯恩富兴'").label("base")


class ResignedEmployeeJinyePO(ResignedEmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_lzpersonal_jy"
    __table_args__ = {"comment": "伯恩金业离职表"}

    base = literal_column("'伯恩金业'").label("base")


class EmployeeBase:
    """在职表基类"""

    ryid = Column(VARCHAR(100), primary_key=True, comment="人员id")
    per_gh = Column(VARCHAR(100), comment="工号")
    per_xm = Column(VARCHAR(100), comment="姓名")
    per_sfzh = Column(VARCHAR(50), comment="身份证号")
    per_lzrq = Column(DateTime, comment="入职日期")
    per_jxfs = Column(VARCHAR(100), comment="计薪方式")
    int_zhiji = Column(VARCHAR(50), comment="职级数")
    per_zw = Column(VARCHAR(50), comment="职位")
    syb_id = Column(VARCHAR(100), comment="事业部id")
    per_syb = Column(VARCHAR(100), comment="事业部")
    dpt_id = Column(VARCHAR(100), comment="厂别id")
    per_dpt = Column(VARCHAR(100), comment="厂别")
    zhu_id = Column(VARCHAR(100), comment="部门id")
    per_zhu = Column(VARCHAR(100), comment="部门")


class EmployeeBaishiPO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_bs"
    __table_args__ = {"comment": "白石园区在职表"}

    base = literal_column("'白石园区'").label("base")


class EmployeeJingmiPO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_jm"
    __table_args__ = {"comment": "精密园区在职表"}

    base = literal_column("'精密园区'").label("base")


class EmployeeGaoxinPO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_gx"
    __table_args__ = {"comment": "高新园区在职表"}

    base = literal_column("'高新园区'").label("base")


class EmployeeMetalPO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_jsc"
    __table_args__ = {"comment": "高新金属厂在职表"}

    base = literal_column("'高新金属厂'").label("base")


class EmployeeFuxingPO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_fx"
    __table_args__ = {"comment": "伯恩富兴在职表"}

    base = literal_column("'伯恩富兴'").label("base")


class EmployeeJinyePO(EmployeeBase, SqlAlchemyBase):
    __tablename__ = "t_personal_jy"
    __table_args__ = {"comment": "伯恩金业在职表"}

    base = literal_column("'伯恩金业'").label("base")
